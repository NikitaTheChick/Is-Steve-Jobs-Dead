import flet as flet
import requests as req

def main(page: flet.Page):
    page.title = "Is Steve Jobs Dead?"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER

    # This function has to fire a get request, decode the JSON, and return the page view assuming the api returned true
    def find_out(e):
        r = req.get("http://api.dummysite.org")

    # This function builds the routes to the page views
    def route_change(route):
        page.views.clear()
        page.views.append(
            flet.View(
                "/",
                [
                    flet.ElevatedButton("Is He Dead?", on_click=lambda _: page.go("/steve")),
                ],
            )
        )
        if page.route == "/steve":
            page.views.append(
                flet.View(
                    "/steve",
                    [
                        flet.ElevatedButton("Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)


flet.app(main, view=flet.AppView.WEB_BROWSER)
