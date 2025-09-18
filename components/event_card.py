from nicegui import ui



def show_event_card(event):
    with ui.card().on(
        type="click",
        handler=lambda: ui.navigate.to(f"/event?id={event["id"]}")
    ).classes("w-[30rem] h-[25rem] cursor-pointer"):
        #ui.label(text=["title"])
        ui.image(source=event["image"])

        ui.label(text=event["title"]).classes('text-bold text-2xl')
        ui.label(text=event["start_date"]).classes("text-blue")
        ui.label(text=event["venue"]).classes('text-gray-700')
