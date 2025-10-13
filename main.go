package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()
	router.LoadHTMLFiles("templates/index.html")
	router.GET("/index", func(c *gin.Context) {
		c.HTML(http.StatusOK, "index.tmpl", gin.H{
			"title": "Is Steve Jobs Dead?",
		})
	})
	router.GET("/steve", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"response": true,
		})
	})
	router.Run()
}
