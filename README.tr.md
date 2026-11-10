English: [README.md](README.md)

# Dünyanın Gözünden Atatürk

[![Serginin açılış görünümü: Atatürk'ün tamamen yazı satırlarından oluşan portresi](viz/public/og.jpg)](https://ataturk.fyi)

1908'den 2026'ya Mustafa Kemal Atatürk hakkında belgelenmiş sözlerden oluşan açık bir arşiv: onun hakkında kimin ne söylediği, nerede söylediği, bunun hangi kaynaktan geldiği ve o kaynağın bağımsız doğrulaması.

Sözler; devlet başkanlarından, şairlerden, generallerden, gazetelerden, parlamentolardan, din adamlarından, düşmanlardan ve hayranlardan geliyor. Her kayıt, belirli bir andaki tek bir sözü konu alan küçük bir YAML dosyasıdır: konuşmacı, tarih, kısa ve tarafsız bir özet, kaynakta yer alıyorsa konuşmacının orijinal dildeki kendi sözleri, kaynak ve bu kaynağı yeniden açıp inceleyen bağımsız bir doğrulayıcının ulaştığı sonuç.

**Sergi:** [ataturk.fyi](https://ataturk.fyi) (Sarmal, Türkçe ve İngilizce). Bu depodaki dosyalardan oluşturulmuştur.

[![Sergide açılmış bir söz: Eleftherios Venizelos, 1934](docs/thread-voice.tr.jpg)](https://ataturk.fyi/?lang=tr#venizelos-1934-01-12)

Her sözün kendi bağlantısı vardır. Yukarıdaki söz [ataturk.fyi/#venizelos-1934-01-12](https://ataturk.fyi/?lang=tr#venizelos-1934-01-12) adresindedir; `#` işaretinden sonraki kısım kaydın `id` değeridir.

## Mevcut boyut

| | |
|---|---|
| Kayıtlar | 976 |
| Farklı söz sahipleri (kişiler, gazeteler, kurumlar, gruplar) | 801 |
| Günümüz ülkeleri ve bölgeleri (`country_now`) | 84; ayrıca Avrupa Birliği, Avrupa Konseyi ve UNESCO |
| Kapsanan yıllar | 1908 – 2026 (106 yıl klasörü; 10 kayıt 1919 öncesindendir; yalnızca 1938'de 207 kayıt vardır) |
| Konuşmacının kendi sözlerini (`quote`) içeren kayıtlar | 31 dilde 849 |
| Kayıtlı kaynak doğrulaması bulunan kayıtlar | 976 (tümü) |
| Türkçe çeviri dosyası bulunan kayıtlar | 976 (tümü) |

Sonuca göre kaynak doğrulamaları:

| Sonuç | Kayıtlar | Oran |
|---|---|---|
| `confirmed` | 776 | %80 |
| `partial` | 96 | %10 |
| `paraphrase-ok` | 57 | %6 |
| `secondary-only` | 31 | %3 |
| `unreachable` | 11 | %1 |
| `not-found` | 3 | %1'in altında |
| `contradicted` | 2 | %1'in altında |

Sonuçların açıklamaları [data/README.md](data/README.md#verdicts) dosyasındadır.

Sergide 970 kayıt gösterilmektedir. Diğer 6 kayıt ise doğrulaması başarısız olan (`not-found`, `contradicted`) 5 kayıt ile Atatürk'ün kendisi hakkında konuştuğu (`voice_type: self`) 1 kayıttır. Bunlar veri setinde kalmaya devam eder.

Söz sahibinin Atatürk'e karşı tutumu (`polarity`): 518 hayranlık duyan (admiring), 139 ikircikli (conflicted), 133 araçsal (instrumental; konuşmacının kendi gündemine hizmet eden övgü), 122 düşmanca (hostile), 64 tanık (witness; bildiren veya katılan, belirtilmiş bir görüşü olmayan).

## Klasörlerin içeriği

| Klasör | İçerik |
|---|---|
| `data/voices/<YYYY>/` | Her kayıt için bir dosya, `<id>.yaml`. `YYYY`, kaydın tarihindeki yıldır. |
| `data/translations/tr/<YYYY>/` | Her kayıt için aynı dosya adıyla Türkçe metin. Makine çevirisidir ve bu şekilde işaretlenmiştir. |
| `data/schema/` | Kayıt ve çeviri dosyaları için JSON Şemaları. |
| `data/templates/voice.yaml` | Yeni bir kayıt için açıklamalı şablon. |
| `data/README.md` | Alan başvuru kılavuzu: her alan, kuralı ve izin verilen değerleri. |
| `vault/` | Doğrulanmış kayıtlardan oluşturulan araştırma notları; her kişi veya olay için bir not, her notun sonunda kaynak listesi. Kayıtlar `node` alanıyla bunlara işaret eder. |
| `research/` | Araştırma sorusu ve yöntemi (`RESEARCH.md`), arama günlüğü (`HUNT.md`), her karar ve düzeltme (`LEDGER.md`), henüz tamamlanmamış ipuçları (`candidates/`) ve kullanılan betikler (`pipeline/`). |
| `tools/` | Doğrulayıcı (`tools/validate.mjs`), yeni kayıt taslak oluşturucusu (`tools/new-voice.mjs`) ve ortak yükleyici (`tools/lib/records.mjs`). |
| `viz/` | Sergi (Vite ve three.js). `viz/scripts/build-data.mjs` verisini `data/` klasöründen oluşturur. |

GitHub bir klasörde en fazla 1.000 dosya gösterdiği için kayıtlar yıl klasörlerine ayrılmıştır.

## Yöntem ve ilkeler

- **Kaynaktan çıkarın, asla ekleme yapmayın.** Her alan belirtilen kaynak tarafından desteklenmelidir. Hiçbir şey hafızadan veya genel kültürden doldurulmaz.
- **Alıntılar birebirdir ve orijinal dilindedir.** Fransızca bir telgraf Fransızca, Rusça bir anı Rusça alıntılanır. İngilizce çevirisi kendi alanında hemen yanında yer alır.
- **Özetler bize aittir ve bizim olarak işaretlenmiştir.** `summary` alanı en fazla 25 kelimelik tarafsız bir açımlamadır. Asla konuşmacının kendi sözleriymiş gibi sunulmaz.
- **Her kayıt, yazarı dışında biri tarafından yeniden doğrulanır.** Doğrulayıcı, belirtilen kaynağı yeniden açar ve bulduklarını aynı dosyanın `verification` bloğuna kaydeder: sonuç, alıntının bulunup bulunmadığı, neyin okunduğu ve nasıl okunduğu.
- **Hem hayranlık dolu hem de düşmanca sözler dahil edilir.** Belgelenmiş bir söz, görüşü ne olursa olsun kaydedilir. Düşmanca bir kayıt bunu kimin, ne zaman ve hangi kaynakta söylediğini belirtir. Arşivin değil, konuşmacının görüşünü kaydeder.
- **Şüpheler kayda geçirilir.** İkinci elden aktarım zincirleri `mediated_by` alanına, belirsizlikler `caveat` alanına yazılır. Doğrulaması başarısız olan kayıtlar veri setinde kalır ancak sergide gösterilmez.
- **Türkçe çeviriler makine yapımıdır ve bu şekilde işaretlenmiştir.** Her çeviri dosyası bunu ilk satırında ve `translated_by` alanında belirtir. Düzeltmeler memnuniyetle karşılanır. Orijinali Türkçe olan metinler basıldıkları haliyle korunur.

## Nasıl katkıda bulunabilirsiniz

Bir söz önerebilir, bir hata bildirebilir, bir kaydı kaynağıyla karşılaştırabilir veya bir Türkçe çeviriyi düzeltebilirsiniz. Hiçbiri için Git veya YAML bilmeniz gerekmez: her birinin bir formu var.

- Formlardan biriyle **bir issue (konu) açın**: [Söz öner / Suggest a voice](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=suggest-voice.yml), [Düzeltme / Correction](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=correction.yml), [Kayıt doğrula / Check a record](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=check-record.yml), [Çeviri düzeltmesi / Translation fix](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=translation.yml).
- **Veya yeni ya da düzeltilmiş bir dosyayla bir pull request (çekme isteği) açın.** Bu işlemi doğrudan tarayıcıda yapabilirsiniz.

**Nereden başlayacağınızı mı düşünüyorsunuz?** Aşağıdakilerin hiçbiri özel bir erişim ya da yazılım gerektirmez:

- **Bir alıntıyı İngilizceye çevirin.** Yaklaşık 300 alıntının henüz İngilizce çevirisi yok; en kalabalık gruplar Türkçe, Fransızca, Felemenkçe, Almanca, Çince, İspanyolca ve Japonca ([#6](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/6)).
- **Bir Türkçe çeviriyi İngilizcesiyle karşılaştırın** ve kulağa yanlış geleni düzeltin. Türkçe metinlerin tamamı makine çevirisidir ([#9](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/9)).
- **Bir kaynağı yeniden açın ve orada ne yazdığını bildirin.** Her kaydın ikinci bir okura ihtiyacı var; [Kayıt doğrula / Check a record](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=check-record.yml) formu birkaç dakikanızı alır. On bir kayıt ise hiç açamadığımız bir kaynağa dayanıyor ([#5](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/5)).
- **Var olduğunu bildiğimiz ama ulaşamadığımız bir metni bulun:** Cinnah'ın Atatürk'ün ölümü üzerine açıklaması ([#8](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/8)), Hemingway'in 1922'de Toronto Star'da çıkan cümlesi ([#7](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/7)), Roncalli'nin günlüğü ([#4](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/4)), Frunze'nin Ankara günlüğü ([#3](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/3)). Bu türden başka ipuçları [`research/candidates/`](research/candidates/) klasöründe ve [`research/HUNT.md`](research/HUNT.md) dosyasının "Open leads that need a person" başlığı altında.

Önce [CONTRIBUTING.tr.md](CONTRIBUTING.tr.md) dosyasını okuyun. Orada neyin bir söz sayıldığı, hangi kanıtların gerektiği ve inceleme sürecinin nasıl işlediği açıklanmaktadır. Tüm proje alanlarında [davranış kuralları](CODE_OF_CONDUCT.md) geçerlidir.

## Veriyi kullanma

Kayıtlar düz YAML dosyalarıdır. Bunları doğrudan okuyabilir veya herhangi bir YAML kütüphanesiyle yükleyebilirsiniz. Alanlar [data/README.md](data/README.md) dosyasında açıklanmıştır; JSON Şeması ise `data/schema/voice.schema.json` içindedir.

Araçlarla çalışmak için Node.js 20 veya daha yeni bir sürüm gerekir:

```sh
npm install
npm run validate   # check every record and translation file against the schema and the rules
npm run export     # write dist/voices.json and dist/voices.csv
```

`dist/voices.json`, `verification` bloğu yalnızca `verdict` değerine indirgenmiş ve kaydın dosya yolu eklenmiş olarak tüm kayıtları tarih sırasına göre tek bir dizide tutar. `dist/voices.csv` ise ana alanları, alıntıyı ve çevirisini, ilk kaynağı ve doğrulama sonucunu içeren, her kayıt için bir satırdan oluşan dosyadır. Byte-order mark (BOM) içeren UTF-8 biçimindedir; böylece hesap tablosu programları Türkçe harfleri doğru gösterir. `dist/` klasörü otomatik oluşturulur ve depoya işlenmez (commit edilmez).

**Lisans.** Veriler, notlar, özetler ve çeviriler (`data/`, `vault/`, betikleri hariç `research/`) [CC BY 4.0](LICENSE-DATA.md) lisansı altındadır. Kodlar (`tools/`, `viz/`, `research/pipeline/`) [MIT lisansı](LICENSE) altındadır. Alıntılar konuşmacılarının kendi sözleri olmaya devam eder; her biri kaynağıyla birlikte kısa alıntılar olarak yeniden üretilmiştir. `viz/public/photos/` içindeki fotoğraflar kamu malıdır (public domain) veya CC0 lisanslıdır; kaynak bilgileri `viz/public/photos/photos.json` dosyasındadır.

## Nasıl kaynak gösterilir

> Okan Erturan, *How the world saw Atatürk: documented voices on Mustafa Kemal Atatürk, 1908–2026*, https://github.com/okanerturan/how-the-world-saw-ataturk (erişim tarihi: 10 Kasım 2026).

Erişim tarihini veriyi kullandığınız tarihle değiştirin. Tek bir kaydı kaynak göstermek için, kaydın `sources` alanında adı geçen orijinal kaynağı belirtin ve kaydın dosya yolunu ekleyin; örneğin `data/voices/1921/lenin-aralov-1921.yaml`.

## Emeği geçenler

Okan Erturan tarafından oluşturulmuştur. Aramaların büyük kısmı yapay zekâ araştırma ajanlarıyla yapıldı. Ardından her kayıt, onu yazmamış olan ikinci bir yapay zekâ ajanı tarafından kaynağıyla karşılaştırılarak yeniden doğrulandı ve bu doğrulama kaydın içine işlendi. Kaynakların çoğunu henüz bir insan yeniden okumadı: siz okursanız, ne bulduğunuzu [Kayıt doğrula](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=check-record.yml) formuyla bildirebilirsiniz.
