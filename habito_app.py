import flet as ft 
def main(page:ft.Page):
    page.theme_mode=ft.ThemeMode.DARK
    page.padding=ft.padding.symmetric(vertical=40)
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.scroll=ft.ScrollMode.AUTO
    page.padding=ft.padding.all(30)
    habts_list=[
        {'titulo':'estudar inglês','done':False,'style':ft.TextStyle(color=ft.colors.BLACK,weight=ft.FontWeight.W_700,size=15),},
        {'titulo':'praticar basquete','done':False,'style':ft.TextStyle(color=ft.colors.BLACK,weight=ft.FontWeight.W_700,size=15),},
        {'titulo':'praticar flet','done':False,'style':ft.TextStyle(color=ft.colors.BLACK,weight=ft.FontWeight.W_700,size=15),},
    ]
    def change(e = None):
        if e:
            for hl in habts_list:
                if hl['titulo']==e.control.label:
                    hl['done']=e.control.value

        done=list(filter(lambda x: x['done'],habts_list))
        total=len(done) / len(habts_list)
        barra.value=total
        text.value=f'{total:.0%}'
        barra.update()
        text.update()
            
    def add_habt(e):
        habts_list.append({'titulo':e.control.value,'done':False,'style':ft.TextStyle(color=ft.colors.BLACK,weight=ft.FontWeight.W_700,size=15),})
        habt.content.controls=[
                        ft.Checkbox(
                            label=hl["titulo"],
                            value=hl["done"],
                            label_style=hl['style'],
                            on_change=change,
                            )for hl in habts_list]
        habt.update()
        e.control.value=''
        e.control.update()
        change()
    layout=ft.Container(
        height=800,
        border_radius=ft.border_radius.all(30),
        bgcolor=ft.colors.BLACK,
        width=400,
        padding=ft.padding.symmetric(vertical=30,horizontal=20),
        content=ft.Column(
            expand=True,
            spacing=5,
            controls=[
                ft.Text(value='que bom ter você aqui',size=20,color=ft.colors.WHITE),
                ft.Text(value='como estão seus hábitos hj?',size=10,color=ft.colors.GREY_400),
                ft.Container(
                    padding=ft.padding.all(20),
                    bgcolor=ft.colors.INDIGO,
                    border_radius=ft.border_radius.all(20),
                    margin=ft.margin.symmetric(vertical=10),
                    content=ft.Column(
                        controls=[
                            ft.Text(value='sua evolução hoje',size=20,color=ft.colors.WHITE),
                        text:= ft.Text(value='0%',size=50,color=ft.colors.WHITE),
                            barra:=ft.ProgressBar(#linha de porcentagem da aplicação
                                value=0,
                                color=ft.colors.INDIGO_900,
                                bgcolor=ft.colors.INDIGO_100,
                                height=15,
                                )
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.CENTER,expand=True,spacing=5
                    ),
                    alignment=ft.alignment.center,height=160
                ),
                ft.Text(value='hábitos de hoje',size=20,color=ft.colors.WHITE),
                ft.Text(value='marcar suas tarefas como concluido te motiva a continuar focado',size=10,color=ft.colors.WHITE),
                habt:=ft.Container(
                    expand=True,
                    padding=ft.padding.all(30),
                    bgcolor=ft.colors.GREY_500,
                    border_radius=ft.border_radius.all(20),
                    margin=ft.margin.symmetric(vertical=10),
                    content=ft.Column(
                        expand=True,
                        scroll=ft.ScrollMode.AUTO,
                        spacing=15,
                        controls=[
                            ft.Checkbox(
                                label=hl["titulo"],
                                value=hl["done"],
                                label_style=hl['style'],
                                on_change=change,
                                )for hl in habts_list]
                    )
                ),
                ft.Text(value='adicionar novo hábito',color=ft.colors.WHITE,),
                ft.TextField(
                    hint_text="escreva um hábito...",
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.GREY_600,
                    border=ft.InputBorder.UNDERLINE,
                    on_submit=add_habt,
                )
            ]
        )
    )
    page.add(layout)
if __name__=="__main__":
    ft.app(target=main,view=ft.WEB_BROWSER)
