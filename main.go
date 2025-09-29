package main

import "github.com/gin-gonic/gin"

func main() {
	router := gin.Default()
	router.GET("/steve", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"response": true,
		})
	})
	router.Run()
}
