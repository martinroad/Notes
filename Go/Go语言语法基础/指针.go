package main

import "fmt"

/**
 * @Description: 引用传递，通过指针将两个变量的值呼唤
 * @param a
 * @param b
 */
func swap(a, b *int) {
	temp := *a
	*a = *b
	*b = temp
}

/**
 * @Description: 利用函数的特性，可以接受多个参数，可以返回多个结果来做交换
 * @param a
 * @param b
 * @return int
 * @return int
 */
func swap1(a, b int) (int, int) {
	return b, a
}

func main() {
	a := 10
	var b *int = &a       // b指向a的地址
	fmt.Println(*b, b)    // 结果为：10 0xc00000a0a0
	fmt.Println(&a, a)    // 结果为：0xc00000a0a0 10
	*b = 100              // 通过b可以修改a的值
	fmt.Println(a, *b, b) // 结果为：100 100 0xc00000a0a0

	// 利用指针进行交换
	c, d := 1, 100
	swap(&c, &d)
	fmt.Println(c, d) // 结果为：100 1

	// 利用函数来进行交换
	e, f := 1, 100
	e, f = swap1(e, f)
	println(e, f) // 结果为：100 1
}
