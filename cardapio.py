<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>PDV Moderno</title>
    <style>
        /* Estilo Geral - Fugindo do "Branco Feioso" */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #1a1a1a; /* Fundo escuro elegante */
            color: #efefef;
            margin: 0;
            display: flex;
            height: 100vh;
        }

        /* Lado Esquerdo - Cardápio/Produtos */
        .menu-section {
            flex: 2;
            padding: 20px;
            overflow-y: auto;
            border-right: 1px solid #333;
        }

        .grid-produtos {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 15px;
        }

        .card-produto {
            background: #2d2d2d;
            border-radius: 12px;
            padding: 10px;
            text-align: center;
            transition: transform 0.2s;
            cursor: pointer;
            border: 1px solid transparent;
        }

        .card-produto:hover {
            transform: translateY(-5px);
            border-color: #4CAF50;
        }

        .card-produto img {
            width: 100%;
            height: 100px;
            object-fit: cover;
            border-radius: 8px;
            background: #444;
        }

        /* Lado Direito - Pagamento */
        .checkout-section {
            flex: 1;
            padding: 20px;
            background-color: #252525;
            display: flex;
            flex-direction: column;
        }

        .titulo { color: #4CAF50; margin-bottom: 20px; }

        .metodos-pagamento {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-top: 20px;
        }

        /* Botões Limpos e Bonitinhos */
        .btn-pay {
            background: #3d3d3d;
            border: none;
            color: white;
            padding: 15px;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }

        .btn-pay:hover { background: #555; }
        .btn-pay.active { background: #4CAF50; } /* Cor de destaque */

        .total-box {
            margin-top: auto;
            font-size: 24px;
            padding: 20px;
            background: #1a1a1a;
            border-radius: 10px;
            text-align: center;
            border: 1px dashed #4CAF50;
        }
    </style>
</head>
<body>

    <!-- LADO ESQUERDO: CARDÁPIO -->
    <section class="menu-section">
        <h2 class="titulo">Cardápio</h2>
        <div class="grid-produtos">
            <!-- Exemplo de Produto -->
            <div class="card-produto">
                <img src="https://placeholder.com" alt="Produto">
                <p>Hambúrguer Art.</p>
                <strong>R$ 25,00</strong>
            </div>
            <!-- Repetir cards aqui -->
        </div>
    </section>

    <!-- LADO DIREITO: PAGAMENTO -->
    <section class="checkout-section">
        <h2 class="titulo">Finalizar Pedido</h2>
        
        <p>Escolha a forma de pagamento:</p>
        <div class="metodos-pagamento">
            <button class="btn-pay">💳 Cartão</button>
            <button class="btn-pay">💵 Dinheiro</button>
            <button class="btn-pay">📱 PIX</button>
            <button class="btn-pay">➕ Outros</button>
        </div>

        <div class="total-box">
            <span>Total: </span>
            <strong>R$ 0,00</strong>
        </div>
        
        <button class="btn-pay active" style="margin-top: 15px; width: 100%;">CONCLUIR VENDA</button>
    </section>

</body>
</html>
