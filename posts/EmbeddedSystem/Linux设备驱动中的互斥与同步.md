Date:2014-1-10
Title:Linux设备驱动开发基础之互斥与同步基础
Slug:Linux设备驱动开发基础之互斥与同步基础
Tags: ES,LDD
#Linux设备驱动开发基础之互斥与同步基础
##一些概念
1. 竟态：多个执行路径对同一资源进行操作时可能引发的资源混乱行为（①）。执行路径为并发源。
2. 临界区：对共享资源的访问代码片段。临界区只能是在一个进程内部而无法跨进程，因为其不是一个对象，我们无法定义一个临界区对象来告知其他进程，而像Mutex和SpinLock都可以。参考[这篇文章](http://blogs.msdn.com/b/larryosterman/archive/2005/08/24/455741.aspx?Redirected=true)。
3. 中断和抢占：一般都是在中断需要返回前会调用重新调度函数，如果没有禁止抢占，那么就会被高优先级的进程抢占。有的地方可以被中断但是进程必须不被抢占，那么只需要禁止抢占就行了。例如spin_lock是可以被中断的，但是不能被抢占,因为被其他进程抢占后会造成死锁。当然因为中断中也可能要去获得这个锁而造成死锁，这个就是spin_lock_irq的来由。
##原子操作与原子变量
- 原子操作：每一步都是不可分割的。
- 原子变量：对此变量的操作（增加或者减小）是原子操作。

`单核处理器+抢占` 与 `多核处理器`在许多发面有类似的特性。

##并发的来源
1. 中断
2. 调度器的可抢占性
3. 多核、多处理器的并发执行

####中断
一般对于本地CPU（就是此刻运行这个代码的CPU或者CPU核），控制其中断使用的函数是：

- local_irq_enable
- local_irq_disable
####调度器的可抢占性
调度器的控制函数：

- preempt_disable
- preempt_enable
####多核、多处理器的并发执行

以上是并发的来源，而下面的方法都是对并发的处理和控制，因此都是**全局的**。
##自旋锁=禁止抢占+原子设置V变量
####特征
1. 对于spin_lock用得比较多的是对全局变量访问时的保护
1. spin_lock是全局的
1. 普通的自旋锁(没有disable_IRQ)有可能会死锁

####自旋锁和信号量的区别
######是否会引发睡眠
自旋锁不会引起调用者睡眠，如果自旋锁已经被别的执行单元保持，调用者就一直循环
查看是否该自旋锁的保持者已经释放了锁，“自旋”就是“在原地打转”。而信号量则引起调
用者睡眠，它把进程从运行队列上拖出去，除非获得锁。

spin_lock，禁止抢占，并且用一个变量来指明资源是否真正被使用。
######是否会造成死锁
spin_lock因为没有禁止中断，所以有可能出现死锁
> 在A进程用自旋锁锁住并使用资源B，处于临界区中，接着被中断，而中断中又去尝试使用资源B，这将造成死锁

#####spin_lock的组成和原理
spin 结构体中里面有个变量，这个变量在spin_lock中被原子改变。因此其他地方再去spin_lock的时候会发现这个变量已经改变，表明锁已经被使用了，此时将在这里自旋等待。
#####spin_lock_irq(Save)变体
1. spin_lock_irq

		spin_lock_irq(Save)=spin_lock + disableIRQ
而普通的spin_lock为

		spin_lock=原子设置V + preempt_disable
这个使得就解决了上面因为中断而造成的死锁的可能性。
2. spin_lock_bh
		
		disable softIRQ
3. 非阻塞版本
		
		spin_trylock：try
#####spin_lock_irq使用注意
1. 任何拥有自旋锁的代码都必须是原子的，不能休眠：例如kmalloc中有GFP_KERNEL掩码时，将有可能造成休眠
2. 在中断中如果要使用自旋锁应该使用`spin_lock_irq`。
##信号量
####特点
允许调用它的进程进入睡眠放入到wait_list中，见下面的结构体成员。
####原理
	/* Please don't access any members of this structure directly */
	struct semaphore {
		spinlock_t		lock;
		unsigned int		count;
		struct list_head	wait_list;
	};
1. lock：一个自旋锁用于对count变量的原子更改。
1. count：记录资源数目。
1. wait_list：将无法获取信号量的进程放入队列中。
####操作
1. DOWN:
2. 
		count--
1. UP:

		count++;唤醒在wait_list中的等待进程
####UP/DOWN的变体
1. down：等待的进程无法被（Ctrl+D）中断,将阻塞在down中。
2. down_interruptible：等待的进程可以被中断，需要检查返回值以确定究竟是什么原因导致的返回。
3. down_trylock：如果无法获取信号量则直接返回而不是进入休眠。
4. up函数只有一个。
##互斥锁
####构成
	struct mutex {
		/* 1: unlocked, 0: locked, negative: locked, possible waiters */
		atomic_t		count;
		spinlock_t		wait_lock;
		struct list_head	wait_list;
	#if defined(CONFIG_DEBUG_MUTEXES) || defined(CONFIG_SMP)
		struct task_struct	*owner;
	#endif
	#ifdef CONFIG_DEBUG_MUTEXES
		const char 		*name;
		void			*magic;
	#endif
	#ifdef CONFIG_DEBUG_LOCK_ALLOC
		struct lockdep_map	dep_map;
	#endif
	};
精简一下就是：

	struct mutex {
		/* 1: unlocked, 0: locked, negative: locked, possible waiters */
		atomic_t		count;
		spinlock_t		wait_lock;
		struct list_head	wait_list;
	};
与上面的semophore相比，就是count的类型从`unsigned int`编程了`atomic_t`,且用1表示没有被锁，0表示锁了。而semophore里面的count则是用来表示可以获取资源的数目。互斥锁就是用来表示一个进程可以获取资源的。
####操作
与semophore一致有UP和DOWN。

##免锁机制RCU：

	RCU = preempt_disable + 每次写都分配一个新空间
####免锁的代价：规则约定
必须在临界区读。
####RCU实现机制
- 写：先重新分配的一个地方，得到一个指针New，然后写进去，接着将这个new指针替换掉指向老数据的老指针Old。这样子完成了数据的刷新。当然指针的替换是原子操作的。最后还需要注册一个回调函数，使得所有对old指针的引用都完成后，用于释放以前分区的空间。
- 释放旧空间：如果只有一个访问，那么读取者的临界区的出口其实就是这个回调函数调用的时机，因为读取者能且仅能在临界区引用指针，但是一个系统很可能有多个CPU运行多个线程去读取和引用old指针，所以当**所有的CPU的发生过一次调度后**（就是绝对不可能在临界区，因为临界区关闭了调度），就可以认为是对老指针引用的完毕。
- 读：构建一个临界区，**并在且只在**临界区内使用指针访问数据。构建临界区的原因是防止在使用指针访问的时候数据被写。

##参考
①来源于深入Linux设备驱动程序内核机制

②[Why don't critical sections work cross process?](http://blogs.msdn.com/b/larryosterman/archive/2005/08/24/455741.aspx?Redirected=true)
