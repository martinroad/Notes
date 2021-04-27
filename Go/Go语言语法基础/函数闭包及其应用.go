//所谓闭包就是能够读取其他函数内部变量的函数

package main

import "fmt"

func main() {
	nextNumber := getSequence()
	fmt.Println(nextNumber()) // 结果为：1
	fmt.Println(nextNumber()) // 结果为：2
	fmt.Println(nextNumber()) // 结果为：3
	fmt.Println(nextNumber()) // 结果为：4
	fmt.Println("---------------------------------------")

	// 从执行结果来看，nextNumber1又从1开始重新开始了，虽然他们函数内部变量名字都是i，但是在不同的函数调用内部，i所在的内存区域也是不同的，因而nextNumber和nextNumber1代表的必然是不同的序列
	nextNumber1 := getSequence()
	fmt.Println(nextNumber1()) // 结果为：1
	fmt.Println(nextNumber1()) // 结果为：2
}

/**
 * @Description: 返回一个函数指针，函数指针内部对变量i进行引用，导致i的内存区域不释放
 * @return func() int
 */
func getSequence() func() int {
	i := 0 // 函数内部变量
	return func() int {
		i += 1
		return i
	}
}
