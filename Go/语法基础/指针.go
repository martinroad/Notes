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

func main() {
	a := 10
	var b *int = &a       // b指向a的地址
	fmt.Println(*b, b)    // 结果为：10 0xc00000a0a0
	fmt.Println(&a, a)    // 结果为：0xc00000a0a0 10
	*b = 100              // 通过b可以修改a的值
	fmt.Println(a, *b, b) // 结果为：100 100 0xc00000a0a0

	c, d := 1, 100
	swap(&c, &d)
	fmt.Println(c, d) // 结果为：100 1
}
