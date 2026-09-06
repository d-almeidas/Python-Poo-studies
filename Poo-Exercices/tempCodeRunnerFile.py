    quercontinuar = input("Deseja continuar? (s/n): ")
    while quercontinuar.lower() not in ['s', 'n']:
        print("[red]Opção inválida! Digite 's' para sim ou 'n' para não.[/red]")
        quercontinuar = input("Deseja continuar? (s/n): ")
    if quercontinuar.lower() == 'n':
        print("[blue]Saindo do sistema...[/blue]")
        break 