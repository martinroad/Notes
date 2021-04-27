package main

import "fmt"

/**
 * @Description:输入a,b两个整数，计算a,b的求和，求差，返回两个int类型结果
 * @param a
 * @param b
 * @return int
 * @return int
 */
func add_sub(a, b int) (int, int) {
	return a + b, a - b
}

/**
 * @Description:输入a,b两个整数，计算a,b的和，返回一个int类型的结果
 * @param a
 * @param b
 * @return int
 */
func add(a, b int) int {
	return a + b
}

func add_func(x int, y int) int {
	return x + y
}

func sub_func(x int, y int) int {
	return x - y
}

/**
 * @Description:要将math_func func(a, b int) int这个看作一个整体，math_func是func(a, b int)的别名，返回一个int类型的结果
 * @param a 参数一
 * @param b 参数二
 * @param math_func 函数func(a, b int)的别名
 * @return int 返回int类型的结果
 */
func count(a int, b int, math_func func(a, b int) int) int {
	return math_func(a, b)
}

func main() {
	x, y := 1, 20

	// 返回2个结果
	sum, sub := add_sub(x, y)
	fmt.Printf("sum:%d\n", sum)
	fmt.Printf("sub:%d\n", sub)

	// 返回1个结果
	sum1 := add(x, y)
	fmt.Println(sum1)

	// 函数指针funcptr
	funcptr := add_sub
	sum1, sub1 := funcptr(x, y)
	fmt.Println(sum1, sub1)

	// 函数指针funcptr作为参数
	sum2 := count(x, y, add_func)
	sub2 := count(x, y, sub_func)
	fmt.Printf("sum2:%d\n", sum2)
	fmt.Printf("sub2:%d\n", sub2)
}
