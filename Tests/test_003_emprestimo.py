def test_002_FazerEmprestismo(common_page, login_page, emprestimo_page, home_page) -> None:
    login_page.login("user1", "pass1")
    home_page.acessarMenu("Empréstimos")
    emprestimo_page.selecionar_valor_emprestimo("2.000,00")
    emprestimo_page.clicar_contratar_emprestimo()
    common_page.verificar_text("A transação foi concluída com sucesso. Você pode voltar para a página principal e continuar suas operações.")
    common_page.voltar_home()
    common_page.verificar_text("7.000,00")
    home_page.acessarMenu("Ver Extrato")
    common_page.verificar_text("Empréstimo contratado - R$ 2000,00")

    

