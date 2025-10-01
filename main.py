import flet as flet
import requests as req

def main(page: flet.Page):
    page.title = "Is Steve Jobs Dead?"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER

    # This function has to fire a get request, decode the JSON, and return the page view
    def find_out(e):
        r = req.get("http://api.dummysite.org")

    # This function builds the routes to the page views
    def route_change(route):
        page.views.clear()
        page.views.append(
            # Start Page View - Displays Animated Steve Graphic with button to initialize app
            flet.View(
                "/",
                [
                    flet.ElevatedButton("Is He Dead?", on_click=lambda _: page.go("/steve")),
                ], horizontal_alignment=flet.CrossAxisAlignment.CENTER
            )
        )
        # Initialized App View - Displays Animated Dead Steve graphic with text stating death status
        if page.route == "/steve":
            page.views.append(
                flet.View(
                    "/steve",
                    [
                        flet.Text("Yea...he's dead"),
                    ], horizontal_alignment=flet.CrossAxisAlignment.CENTER
                )
            )
        # Error Page View (Displays if communication with server interrupted) - Error Graphic with text and return to home button
        if page.route == "/dead":
            page.views.append(
                flet.View(
                    "/dead",
                    [
                        flet.ElevatedButton("Home", on_click=lambda _: page.go("/")),
                    ], horizontal_alignment=flet.CrossAxisAlignment.CENTER
                )
            )
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)


flet.app(main, view=flet.AppView.WEB_BROWSER)
