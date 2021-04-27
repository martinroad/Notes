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
func test_switch(code int) {
	fmt.Printf("code:%d\n", code)
	switch code {
	case 1:
		fmt.Printf("swith：%d\n", code)
	case 2:
		fmt.Printf("swith：%d\n", code)
	case 3:
		fmt.Printf("swith：%d\n", code)
	case 4:
		fmt.Printf("swith：%d\n", code)
	case 5:
		fmt.Printf("swith：%d\n", code)
	default:
		fmt.Println("switch default")
	}
}

/**
 * @Description: 测试 for 循环
 * @param count
 */
func test_for(count int) {

}

func main() {
	// 测试if...else if...if
	x := 10
	if_test(x)

	// 测试switch，接受标准的输入
	var code int
	fmt.Scanf("请输入一个整数:%d\n", &code)
	println(code, &code)
	test_switch(code)
}
