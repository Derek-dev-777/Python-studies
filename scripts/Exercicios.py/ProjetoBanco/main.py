from contas import ContaCorrente,ContaPoupança

conta1 = ContaCorrente("Santander", 23213)

print(conta1)
conta1.depositar(500,"Santander")
print(conta1)
conta1.sacar(501,"Santander")
print(conta1)