import flet as ft

def main(page: ft.Page):

    # /* レイアウト関連 */
    page.window_width = 450  # 幅
    page.window_height = 300  # 高さ
    # page.window_top = 100  # 位置(TOP)
    # page.window_left = 100  # 位置(LEFT)
    page.window_always_on_top = True  # ウィンドウを最前面に固定
    page.update()

    dd = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )

    page.title = "Flet counter example" # 3.
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # 4.

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100) # 5.

    def minus_click(e): # 6.
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e): # 6.
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()


    t = ft.Tabs(
        selected_index=1,
        animation_duration=400,
        tabs=[
            ft.Tab(
                text="サーバ接続",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="フォルダ管理",
                # tab_content=ft.Icon(ft.icons.FOLDER_OPEN),
                icon=ft.icons.FOLDER_OPEN,
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Tab 3",
                icon=ft.icons.SETTINGS,
                content=ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    txt_number,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
                # content=ft.ElevatedButton(text="Submit")
            ),
        ],
        expand=1,
    )


    # def button_clicked(e):
    #     t2.value = "recomended!"
    #     t2.update()

    # b1 = ft.FilledTonalButton(
    #     text="わたしを推してください",
    #     icon=ft.icons.RECOMMEND,
    #     on_click=button_clicked,
    # )


    # async def button_clicked(e):
    #     t.value = f"Dropdown value is:  {dd.value}"
    #     await t.update_async()

    # t = ft.Text()
    # b = ft.ElevatedButton(text="Submit", on_click=button_clicked)

    # t2 = ft.Text()
    # page.add(b1, t2)
    page.add(t)

ft.app(target=main)
