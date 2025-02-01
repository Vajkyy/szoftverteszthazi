import fuggveny


def sorta_sum_test():
    elso_lista = [3, 9, 10, 12, -3, 4, 4, 14, 14]
    masodik_lista = [4, 4, 11, -3, 12, 5, 6, 7, 6]
    vart_lista = [7, 20, 21, 9, 9, 9, 20, 21, 20]

    for i in range(len(elso_lista)):
        print(f"{i + 1}. teszteset:")
        elso = elso_lista[i]
        masodik = masodik_lista[i]
        vart = vart_lista[i]
        kapott = fuggveny.sorta_sum(elso, masodik)
        print(f"első szám: {elso}, második szám: {masodik}, várt: {vart}, kapott: {kapott}, JÓ_E? {vart == kapott}")


