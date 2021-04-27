package main

import "fmt"

/**
 * @Description: 测试 if ...else if...else 条件分支
 * @param x
 */
func if_test(x int) {
	if x > 10 {
		fmt.Println(" x biger than 10")
	} else if x == 10 {
		fmt.Println("x equal 10")
	} else {
		fmt.Println("x less than 10")
	}
}

/**
 * @Description: 测试 switch 分支
 * @param code
 */
func test_switch(age int) {
	switch age {
	case 1:
		fmt.Printf("swith：%d\n", age)
	case 2:
		fmt.Printf("swith：%d\n", age)
	case 3:
		fmt.Printf("swith：%d\n", age)
	case 4:
		fmt.Printf("swith：%d\n", age)
	case 5:
		fmt.Printf("swith：%d\n", age)
	default:
		fmt.Println("switch default")
	}
}

/**
 * @Description: 测试 for 循环的三种方式
 * @param count
 */
func test_for(count int) {
	// 第一种方式 for init; condition; position { }
	i, sum := 0, 0
	for i = 0; i <= 100; i++ {
		sum += i
	}
	fmt.Printf("sum is %d", sum)

	//	第二种方式 for condition { }
	i, sum = 0, 0
	for i <= count {
		sum += i
		i++
	}
	fmt.Printf("sum is %d", sum)

	//	第二种方式 for {}，类似于四循环
	// 示例：每隔1秒钟，打印 hahaha~
}

func main() {
	// 测试if...else if...if
	x := 10
	if_test(x)

	// 测试switch，接受标准的输入
	var (
		name string
		age  int
	)
	fmt.Println("请输入姓名和年龄：")
	//fmt.Scanf("name:%s\n", &name) // 输入内容，name:lllll
	fmt.Scanf("%s %d\n", &name, &age) // 输入内容，小明 2
	println(name, &name)              //结果为：小明 0xc0001041e0
	println(age, &age)                //结果为：2 0xc00000a0c0
	test_switch(age)

	// 测试for循环
	var count int
	fmt.Println("请输入一个整数，计算求和：")
	fmt.Scanf("%d", &count)
	test_for(count)
}
