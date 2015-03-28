package main

import "fmt"

func main() {
	html :=
		`Content-type:text/html

<html>
<head>
	<title>Hello Word - First CGI Program</title>
</head>
<body>
	<h2>Hello Word! This is my first CGI program</h2>
</body>
</html>`
	fmt.Println(html)
}
