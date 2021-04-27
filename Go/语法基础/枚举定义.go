package main

// 定义业务数据，iota是golang语言的常量计数器,只能在常量的表达式中使用
const (
	A = iota // iota = 0
	B        // 结果为：1
	C        // 结果为：2
	D        // 结果为：3
	_
	_
	E            // 结果为：6
	F = iota + 2 //结果为：9，这时候iota = 7, 7 + 2 = 9
)

func main() {
	println(A, B, C, D, E, F)
}
