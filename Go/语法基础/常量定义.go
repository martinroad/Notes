//在Go语言中，使用const 关键字定义常量，所谓常量，就是在程序运行时，值不会被修改的标识

package main

import "fmt"

func main() {
	const LEGTH int32 = 10
	const WIDTH int32 = 5
	const a, b, c = 1, false, "hello"

	// 注意用 := 定义变量area，冒等不适合用于常量
	area := LEGTH * WIDTH

	//Printf 与 Printfln 的区别是格式化以及自动换行
	fmt.Printf("area is %d", area)
	fmt.Println(a, b, c)
}
