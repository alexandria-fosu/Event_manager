from nicegui import ui


def show_navbar():
    
    with ui.row():
        ui.link("Home","/home")
        ui.link("signup","/signup")
        ui.link("signin", "/signin")
        ui.link("create Event", "/create_event")
        ui.link("event", "/event")
        ui.link("college", "/college")
        ui.link("not found", "/not_found")