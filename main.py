# Bu script, basit bir kripto para portföyünün toplam değerini hesaplar.

def calculate_portfolio_value(portfolio, prices):
    """
    Portföydeki varlıkların toplam değerini hesaplar.
    :param portfolio: {'BTC': 0.5, 'ETH': 10} gibi bir sözlük (varlık ve miktarı)
    :param prices: {'BTC': 70000, 'ETH': 3500} gibi bir sözlük (varlık ve anlık fiyatı)
    :return: Portföyün toplam değeri (float)
    """
    total_value = 0.0
    print("--- Portföy Detayları ---")
    for coin, amount in portfolio.items():
        # Eğer portföydeki coinin fiyatı prices listesinde varsa hesapla
        if coin in prices:
            value = amount * prices[coin]
            # f-string formatlama ile sayıyı para birimi gibi gösteriyoruz (örn: 4,250.75)
            print(f"{amount} {coin} = ${value:,.2f}")
            total_value += value
        else:
            print(f"-> {coin} için fiyat bulunamadı, hesaplama dışı bırakıldı.")
    
    return total_value

if __name__ == "__main__":
    # 1. Adım: Elimizdeki varlıkları ve miktarlarını tanımlayalım.
    # Bu kısmı kendi portföyünüze göre değiştirebilirsiniz.
    my_portfolio = {
        'BTC': 0.05,
        'ETH': 1.2,
        'SOL': 5,
        'XRP': 250,
        'ADA': 500,
    }

    # 2. Adım: Varlıkların anlık Dolar fiyatlarını tanımlayalım.
    # Bu fiyatlar temsilidir, anlık değildir.
    current_prices = {
        'BTC': 68000.50,
        'ETH': 3550.75,
        'SOL': 150.25,
        'ADA': 0.45  # Portföyde olmayan bir coinin fiyatını ekleyelim
    }

    # 3. Adım: Fonksiyonu çağırarak toplam değeri hesaplayalım.
    total_portfolio_value = calculate_portfolio_value(my_portfolio, current_prices)

    print("--------------------------")
    # Toplam değeri de para birimi gibi formatlayarak yazdıralım
    print(f"Toplam Portföy Değeri: ${total_portfolio_value:,.2f}")