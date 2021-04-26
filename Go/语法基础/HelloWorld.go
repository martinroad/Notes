package main // 包名，如果是主函数所在问津，包名必须是main

import (
	"fmt" // import 导入包名
)

/**
 * @Description: main 函数入口
 */
func main() {
	fmt.Println("Hello World") // 包名.函数名()

	var x1 uint
	var x, y, z = 1, 23, "hello"
	u, t := 456, "World"
	d := 789
	h := 100
	fmt.Println(x1, x, y, z, u, t, d, h)
}
