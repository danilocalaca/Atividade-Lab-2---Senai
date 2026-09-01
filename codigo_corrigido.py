# Módulo de Autenticação Corrigido

import hashlib
import logging

# Configuração dos logs
logging.basicConfig(
    filename="autenticacao.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def gerar_hash(senha):
    """Gera o hash SHA-256 da senha."""
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()


# Senhas armazenadas como hash
usuarios_db = {
    "admin": gerar_hash("admin123"),
    "gerente": gerar_hash("senha456")
}


def login(usuario, senha):
    """Realiza a autenticação do usuário."""

    if usuario not in usuarios_db:
        logging.warning(f"Tentativa de login de usuário inexistente: {usuario}")
        print("Falha na autenticação")
        return False

    senha_hash = gerar_hash(senha)

    if usuarios_db[usuario] == senha_hash:
        logging.info(f"Acesso liberado para {usuario}")
        print(f"Acesso liberado para {usuario}")
        return True

    logging.warning(f"Falha de autenticação para {usuario}")
    print("Falha na autenticação")
    return False


# Testes
if __name__ == "__main__":
    login("admin", "admin123")
    login("admin", "senha_errada")
    login("usuario_inexistente", "123456")
