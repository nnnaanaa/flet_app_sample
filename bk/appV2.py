import flet as ft

def main(page: ft.Page):

    # /* レイアウト関連 */
    page.window_width = 450  # 幅
    page.window_height = 300  # 高さ
    page.window_always_on_top = True  # ウィンドウを最前面に固定
    page.update()

    # ft.CupertinoTextField(
    #     placeholder_text="Only numbers are allowed :)",
    #     input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
    # )

    # dd = ft.Dropdown(
    #     width=100,
    #     options=[
    #         ft.dropdown.Option("Red"),
    #         ft.dropdown.Option("Green"),
    #         ft.dropdown.Option("Blue"),
    #     ],
    # )

    async def button_clicked(e):
        t.value = f"Dropdown value is:  {dd.value}"
        await t.update_async()


    t = ft.Text()
    dd =  ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
    eb1 = ft.ElevatedButton("登録", icon=ft.icons.ADD)
    sw = ft.Switch(
        label="ラベル", value=True,
    )

    card = ft.Card(ft.Container(ft.Column([
        dd,
        ft.ElevatedButton(text="Submit", on_click=button_clicked),
        eb1,
        sw,
        t,
    ]),
        padding=10,
        width=400,
    ),
        margin=10,
        elevation=5,
    )

    page.add(card)

ft.app(target=main)
