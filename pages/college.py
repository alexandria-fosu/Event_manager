from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer


@ui.page("/college")
def show_college_page():
    show_navbar()
    
    with ui.card().classes("w-full h-full mx-auto p-6 bg-white rounde-xl mt-10"):
        ui.image("assets/d781c2225f9b6f40dc46825ab74d11a980025545.jpg").classes("w-full h-full rounded-lg mb-4 ")
        ui.label("IIT Roorke").classes("text-2xl font-bold")
        ui.label("Often cited for its leadership in science, engineering, and technology, MIT is celebrated for its rigorous academics and a culture of innovation. Located in Cambridge, Massachusetts, its graduates are highly sought after by top companies and research institutions worldwide.").classes("text-gray-700 text-xl")
        ui.label("The university is a hub for groundbreaking research, and its alumni have founded countless successful companies.").classes("text-grey-700 text-xl")
        ui.label("Often cited for its leadership in science, engineering, and technology, MIT is celebrated for its rigorous academics and a culture of innovation. Located in Cambridge, Massachusetts, its graduates are highly sought after by top companies and research institutions worldwide.").classes("text-gray-700 text-xl")
        ui.label("The university is a hub for groundbreaking research, and its alumni have founded countless successful companies.").classes("text-grey-700 text-xl")


    with ui.row().classes(' mt-10 '):
            ui.label("Our").classes('text-bold text-4xl')
            ui.label("Blogs").classes('text-bold text-blue text-3xl')

    with ui.grid(columns=3).classes("w-full mb-50"):
        for i in range(6):
            with ui.card().classes("w-[30rem] h-[25rem]"):
                ui.image("assets/2661d4f20d55464672c777fe2598b4a832227655.jpg")

                ui.label("Bestseller Book Bootcamp-write, Market & Publish your books-Lucknow").classes('text-bold text-2xl')
                ui.label("Sunday 16 November").classes("text-blue")
                ui.label("online-event: join anywhere").classes('text-gray-700')



    show_footer()



    