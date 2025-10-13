import flet as flet
import requests as req
import threading

def main(page: flet.Page):
    page.title = "Is Steve Jobs Dead?"
    page.adaptive = True
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.fonts = {
        "Planet Benson": "/fonts/planetbe.ttf"
    }

    evnt = threading.Event()
    jobs1 = flet.Image(src="/steve_jobs.png", fit=flet.ImageFit.CONTAIN, scale=0.6, top=0, left=-800, border_radius=400, animate_position=flet.Animation(150, flet.AnimationCurve.EASE_OUT))
    jobs2 = flet.Image(src="/dead_jobs.png", fit=flet.ImageFit.CONTAIN, scale=0.6, top=0, left=-200, border_radius=400, animate_position=flet.Animation(1000, flet.AnimationCurve.EASE_OUT))

    # This function has to fire a get request, decode the JSON, and return the page view
    def find_out(e):
        r = req.get("http://api.dummysite.org")
        if r.json() == [{"response": True}]:
            page.go("/steve")
        else:
            page.go("/dead")
        evnt.wait(1)
        if jobs2.left != -200:
            jobs2.left = -200
        jobs2.update()

    def animate(e):
        if jobs1.left != -200:
            jobs1.left = -200
        jobs1.update()
        evnt.wait(1)
        page.go("/steve")

    # This function builds the routes to the page views
    def route_change(route):
        page.views.clear()
        page.views.append(
            # Start Page View - Displays Animated Steve Graphic with button to initialize app
            flet.View(
                "/",
                [
                    flet.Stack(
                        [
                            #flet.Image(src="/steve_jobs.png", fit=flet.ImageFit.CONTAIN, border_radius=200),
                            jobs1,
                            flet.Row(
                                [
                                    flet.Text("Is Steve Jobs Dead?!", size=28, font_family="Planet Benson")
                                ],
                                alignment=flet.MainAxisAlignment.CENTER,
                                top=20,
                            )
                        ],
                        width = 360,
                        height = 640,
                    ),
                    flet.ElevatedButton(content=flet.Text("Is He Dead?!", size=20, weight=flet.FontWeight.BOLD), on_click=animate)
                ], horizontal_alignment=flet.CrossAxisAlignment.CENTER
            )
        )
        if page.route == "/steve":
            page.views.append(
                flet.View(
                    "/steve",
                    [
                        flet.Stack(
                        [
                            #flet.Image(src="/steve_jobs.png", fit=flet.ImageFit.CONTAIN, border_radius=200),
                            #ft.Container(content=ft.CircleAvatar(bgcolor=ft.Colors.GREEN, radius=5), alignment=ft.alignment.bottom_left),
                            jobs2,
                            flet.Row(
                                [
                                    flet.Text("Yea he's dead...", size=28, font_family="Planet Benson")
                                ],
                                alignment=flet.MainAxisAlignment.CENTER,
                            ),
                        ],
                        width = 360,
                        height = 640,
                    )
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


flet.app(main, assets_dir="assets", view=flet.AppView.WEB_BROWSER)
