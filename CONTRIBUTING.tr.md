English: [CONTRIBUTING.md](CONTRIBUTING.md)

# Katkıda Bulunma

Bu arşiv, insanların kaynaklarda buldukları sözleri eklemesi ve gördükleri hataları düzeltmesiyle büyür. Bu sayfada nelerin kabul edildiği, hangi kanıtların gerektiği, bunların nasıl gönderileceği ve sonrasında ne olacağı anlatılmaktadır.

Issue (konu) ve pull request (çekme isteği) açıklamalarını Türkçe veya İngilizce yazabilirsiniz.

## Nereden başlamalı?

Elinizde bir söz ve kaynağı varsa [Yardım etmenin üç yolu](#yardım-etmenin-üç-yolu) bölümüne geçin. Yardım etmek istiyor ve yapacak bir iş arıyorsanız, şu an açık olanlar şunlar:

- Yaklaşık 300 alıntının İngilizce çevirisi yok ([#6](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/6)).
- Türkçe çeviriler makineyle yapıldı ve okunmayı bekliyor ([#9](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/9)).
- Her kaydın kaynağını yeniden açacak birine ihtiyacı var: [Bir kaydı doğrulama](#bir-kaydı-doğrulama) bölümüne bakın. On bir kayıt, kimsenin açamadığı bir kaynağa dayanıyor ([#5](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/5)).
- Var olduğu bilinen ama ulaşılamayan metinler var. Başlığı "Wanted" ile başlayan issue'lar bunlardan dördünü anlatıyor; [`research/candidates/`](research/candidates/) klasörü ile [`research/HUNT.md`](research/HUNT.md) dosyasındaki "Open leads that need a person" bölümü bölgelere göre daha fazlasını sıralıyor.

## Ne bir söz sayılır?

Bir söz; kimliği belirli bir kişinin, gazetenin, kurumun veya topluluğun bilinen bir zamanda, işaret edebileceğiniz bir kaynakta Atatürk hakkında görüş bildirmesidir. Arşivde halihazırda yer alan bazı örnekler:

- bir kişi: Rabindranath Tagore'un Kasım 1926'da İstanbul basınına Türkiye Cumhurbaşkanı'nın "bize uygarlığın yolunu gösterdiğini" söylemesi (`data/voices/1926/rabindranath-tagore-1926.yaml`);
- bir gazete: İsveç'te yayımlanan günlük Aftonbladet gazetesinin Kasım 1938'deki yazısı (`data/voices/1938/aftonbladet-1938.yaml`);
- bir kurum: 1922'deki Komünist Enternasyonal Dördüncü Kongresi (`data/voices/1922/comintern-4th-congress-1922.yaml`);
- bir topluluk: Ekim 1922'de Cheribon'da toplanan Cava Müslümanları El-İslam Kongresi (`data/voices/1922/al-islam-congress-cheribon-1922-10.yaml`). Bir topluluğun tek bir isimli sözcüsü yoktur, ancak kaynak grubu, yeri ve tarihi belirtir.

Önemli şahsiyetler (devlet başkanları, tanınmış yazarlar, bilim insanları, dini liderler) için, herhangi bir görüş belirtmeseler bile kendisiyle belgelenmiş doğrudan temaslar da (bir görüşme, ziyaret, mektup) kabul edilir. Eylül 1936'da VIII. Edward'ın ziyareti buna bir örnektir (`data/voices/1936/edward-viii-1936-09.yaml`). Bu tür kayıtlarda genellikle `polarity: witness` bulunur.

Bir kayıt, tek bir andaki tek bir sestir. Aynı kişi onun hakkında farklı görüşlerle veya yıllar arayla iki kez konuştuysa, bu iki ayrı kayıttır.

## Neler kabul edilmez?

- Sizin veya bir başkasının, bir kaynakta yayımlanmamış Atatürk hakkındaki kişisel görüşleri.
- Kaynağı olmayan veya gösterilen kaynağın ilgili metni içermediği iddialar.
- Özel kişilerin sosyal medya paylaşımları.
- Önerilerde veya yorumlarda yer alan hakaretler.
- Bu arşiv için yazılmış her şey: bize yapılmış veya bizim isteğimiz üzerine verilmiş açıklamalar. Bir söz, arşivden bağımsız olarak var olan bir kaynaktan gelmelidir.
- Kaynak olarak alıntı siteleri, söz derlemeleri ve üzerinde alıntı bulunan görseller. Bilinen bir sözün izi sürülebilir bir kaynağı yoksa, o kişinin sözü olarak arşive giremez. İlk nerede basıldığını bulabilirseniz, o kaynak bir katkıdır.

## Kanıt standartları

- **Birincil kaynakları tercih edin:** konuşmacının kendi metni, dönemin bir gazetesi, meclis tutanağı, mektup, arşiv belgesi. Birincil kaynağı alıntılayan akademik bir kitap veya makale de uygundur; aktarım zincirini `mediated_by` alanına kaydedin, örneğin `"Toksoy 2006 ← Cumhuriyet 14 Nov 1938"`.
- **Sayfa numarasını verin.** Kitap, dergi veya basılı gazete için sayfa (veya sütun ya da varak) numarasını belirtin. Web sitesi için bağlantıyı ve mümkünse [Wayback Machine](https://web.archive.org/) üzerindeki arşivlenmiş kopyasını verin.
- **Özgün dilinde, birebir alıntı yapın.** Kelimeleri eski imla dahil kaynakta basıldığı şekliyle, olduğu gibi kopyalayın. Çıkarılan kelimeleri `…` ile gösterin. Alıntı İngilizce değilse, kendi alanına (`quote.translation`) İngilizce çevirisini ekleyin. Özgün metnin yerine çeviri koymayın. Kaynağın kendisi yalnızca bir çeviri veriyorsa (örneğin Almanca yapılmış bir konuşmanın bir Türk gazetesindeki hâli), onu basıldığı gibi alıntılayın ve `quote.is_translation: true` yazın.
- **Özet bize aittir.** `summary`, söz sahibinin onda ne gördüğünü 25 veya daha az kelimeyle, İngilizce ve tarafsız biçimde yeniden ifade eden bir özettir. Ne söylediklerini aktarır ("Onu … olarak nitelendirdi", "… övdü", "… kınadı") ve bizim kendi yargımızı katmaz.
- **Konuşanı kaynağın tanıttığı gibi tanıtın.** `role`, konuştuğu sırada kim olduğunu birkaç kelimeyle söyler. Sonradan ne olduğunu yazmayın.
- **Şüphelerinizi yazın.** Yalnızca tek bir kaynak varsa, tarih yaklaşık ise veya sözün kime ait olduğu kesin değilse, bunu `caveat` alanında belirtin.
- **Polarite (`polarity`), kaynağın gösterdiği şekliyle konuşmacının tutumudur.** Bizim konuşmacı hakkındaki görüşümüz veya Atatürk hakkındaki görüşümüz değildir.

Alanların ve izin verilen değerlerin tam listesi [data/README.md](data/README.md) dosyasındadır.

## Yardım etmenin üç yolu

Kolaydan zora doğru sıralanmıştır. Bir kaydın `summary` ve `role` alanları İngilizce yazılır. Türkçe yazmayı tercih ederseniz bir issue formu kullanın; bakımcı (proje sorumlusu) veya başka bir katkıda bulunan kaydı buradan oluşturabilir.

### 1. Form kullanarak bir issue açın

Yalnızca bir GitHub hesabına ihtiyacınız vardır. Bir form seçin:

- [Suggest a voice / Söz öner](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=suggest-voice.yml): henüz arşivde olmayan bir söz.
- [Correction / Düzeltme](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=correction.yml): bir kayıttaki hatalı bir bilgi.
- [Check a record / Kayıt doğrula](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=check-record.yml): bir kaydın kaynağını yeniden açtınız ve orada ne yazdığını söyleyebilirsiniz.
- [Translation fix / Çeviri düzeltmesi](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=translation.yml): daha iyi bir Türkçe ifade önerisi.

Bir söz önermeden önce, halihazırda mevcut olup olmadığını görmek için ismi [sergide](https://the-long-thread.pages.dev) veya bu depoda arayın. Bakımcı veya başka bir katkıda bulunan, uygun bir öneriyi kayda dönüştürür ve issue içinde bağlantısını paylaşır.

### 2. Tarayıcı üzerinden dosya ekleyin veya düzenleyin

Herhangi bir yazılıma gerek yoktur; GitHub'ın web düzenleyicisi yeterlidir.

Kayıt eklemek için:

1. [Şablonu](data/templates/voice.yaml) açın, "Raw" düğmesine tıklayın ve tamamını kopyalayın.
2. `data/voices/` dizinine gidin ve sözün tarihine ait yıl klasörünü açın, örneğin `data/voices/1938/`.
3. "Add file" ve ardından "Create new file" düğmesine tıklayın. GitHub önce depoyu çatallamanızı (fork) isteyecektir; kabul edin.
4. Dosyaya `<id>.yaml` biçiminde ad verin, örneğin `firstname-lastname-1938.yaml`. İlgili yıl için henüz bir klasör yoksa, `data/voices/` dizininden başlayın ve dosya adından önce yılı ve eğik çizgiyi yazın, örneğin `1951/firstname-lastname-1951.yaml`; GitHub klasörü oluşturur.
5. Şablonu yapıştırın ve doldurun. Kullanmadığınız isteğe bağlı satırları silin veya yorum satırı olarak bırakın.
6. "Commit changes…" ve ardından "Propose changes" düğmesine tıklayın. GitHub bir pull request sayfası açar; "Create pull request" düğmesine tıklayın.

Bir kaydı düzeltmek için dosyasını açın, kalem simgesine ("Edit this file") tıklayın, değişikliği yapın ve 6. adımdan devam edin.

Ardından pull request üzerinde otomatik doğrulama çalışır. Bir sorun bildirirse ilgili satırı işaret eder. Pull request'inizin "Files changed" sekmesinden dosyayı açıp yeniden düzenleyin; pull request kendiliğinden güncellenir.

### 3. Kendi bilgisayarınızda çalışın

Git ve Node.js 20 veya daha yeni bir sürüm gerekir. GitHub'da depoyu çatallayın (fork), kendi çatalınızı klonlayın ve klasörün içinde şu komutları çalıştırın:

```sh
npm install
npm run new -- "Voice Name" 1938-11-10   # writes data/voices/1938/voice-name-1938.yaml from the template
# fill in the new file
npm run validate                          # must end with OK
```

`npm run new` komutu `id`, `voice`, `date` ve tarihten anlaşılıyorsa `era` alanlarını doldurur. Hiçbir zaman mevcut bir dosyanın üzerine yazmaz. Kimlik (`id`) alınmışsa veya isimde Latin harfleri yoksa (Çince, Arapça, Rusça …), kimliği `--id` ile kendiniz verin; örneğin `npm run new -- "Voice Name" 1938-11-10 --id voice-name-1938-11-10`. `npm run validate -- <file>` komutu yalnızca tek bir dosya için rapor verir.

Ardından değişiklikleri kaydedin (commit), kendi çatalınıza gönderin (push) ve bir pull request açın.

## Türkçe çeviriyi düzeltme

Her kaydın Türkçe metni, kayıtla aynı yıl klasörü ve dosya adıyla `data/translations/tr/<YYYY>/<id>.yaml` içinde yer alır. Bu dosyalar makine çevirisiyle oluşturulmuştur ve pek çoğu iyileştirilebilir.

1. Dosyayı açın ve Türkçe metni düzenleyin.
2. `source_fingerprints` alanını olduğu gibi bırakın. Bu alan, ilgili verinin hangi İngilizce metinden çevrildiğini kaydeder; Türkçeyi düzeltmek bunu değiştirmez.
3. Kendinizi `reviewed_by` alanına ekleyin:

   ```yaml
   reviewed_by:
     - your-github-handle
   ```

`quote_kind` değeri `original-turkish` olduğunda alıntı, konuşmacının kayıttan kopyalanmış kendi Türkçe sözleridir. Bunu yalnızca kaynağa uyması için düzeltin ve kayıttaki `quote.text` alanını da düzeltin.

Dosya düzenlemeyi tercih etmiyorsanız [Translation fix / Çeviri düzeltmesi](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=translation.yml) formunu kullanın.

## Bir kaydı doğrulama

Her kayıt, onu ekleyen kişi dışında biri tarafından doğrulanmalıdır. Doğrulamayı yapan kişi belirtilen kaynağı yeniden açar; alıntıyı, konuşanı, tarihi ve vesileyi kontrol eder.

Doğrulamanızı göndermek için [Check a record / Kayıt doğrula](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=check-record.yml) formunu kullanın: kaydı belirtin, neyi açtığınızı (bağlantıyı ya da kitabı ve sayfasını) ve sözlerin kayıttaki gibi olup olmadığını yazın. Fark varsa kaynaktaki ifadeyi aynen aktarın. Bakımcı, sonucunuzu `checked_by` alanına adınızı yazarak kaydın `verification` bloğuna işler (bkz. [data/README.md](data/README.md#verification)).

Sorun bulan bir doğrulama, onaylayan bir doğrulama kadar değerlidir. Doğrulamadan geçemeyen kayıtlar veride işaretli olarak kalır, sergiden çıkar.

Kendi eklediğiniz bir kayda asla `verification` bloğu eklemeyin.

## Katkıda bulunduktan sonra ne olur?

1. **Otomatik doğrulama.** Doğrulayıcı (`npm run validate`) her pull request üzerinde çalışır. Birleştirme (merge) öncesinde hatalar düzeltilmelidir; uyarılar ve bildirimler birleştirmeyi engellemez.
2. **Bakımcı incelemesi.** Bakımcı, kaydı kaynağıyla karşılaştırarak okur; değişiklik isteyebilir veya küçük düzenlemeler yapabilir. Doğrulayıcı, bakımcının incelemesi için `verification` bloğundaki her türlü değişikliği işaretler.
3. **Birleştirme.** Birleştirilen bir kayıt anında verinin parçası olur. Sergide görünmesi ise ancak yazarı dışında birinin kaynağı yeniden açıp `verification` alanını doldurmasından sonra gerçekleşir.

Bir issue, yeni veya düzeltilmiş kayda verilen bir bağlantıyla ya da kabul edilmeme gerekçesiyle kapatılır.

## Moderasyon ve hukuk

Bu arşiv Türkiye'den yayımlanmaktadır. 5816 sayılı Kanun (Atatürk Aleyhine İşlenen Suçlar Hakkında Kanun) uyarınca Atatürk'ün hatırasına alenen hakaret etmek suçtur.

Arşiv, tarihteki söz sahiplerinin onun hakkında ne söylediğini her biri kendi kaynağıyla birlikte belgeler. Karşıt veya düşmanca sözler de buna dahildir. Düşmanca bir görüş içeren kayıt; bunu kimin, ne zaman söylediğini ve nerede basıldığını tarafsız bir özet ve kısa, birebir bir alıntıyla aktarır. Konuşmacının görüşünü kaydeder; o görüşü benimsemez.

Her katkı birleştirilmeden önce bakımcı tarafından incelenir. Kişisel görüş veya hakaret içeren issue'lar, pull request'ler ve yorumlar kapatılır. [Davranış kurallarına](CODE_OF_CONDUCT.md) bakın.

## Yapay zeka araçları

Sözleri aramak, kaynak bulmak veya çeviri taslağı çıkarmak için yapay zeka araçlarını kullanabilirsiniz. Ancak kaynaktaki ilgili bölümü bizzat okumuş olmanız gerekir: özeti değil; sayfanın kendisini, taramasını veya basılı metni görmelisiniz. Kaynakta bizzat görmediğiniz bir alıntıyı asla göndermeyin. Yapay zeka araçları gerçek gibi görünen ama var olmayan alıntılar, sayfa numaraları ve kaynakçalar üretebilir.

Bir şeyi bulmanıza bir yapay zeka aracı yardımcı olduysa, bunu issue veya pull request içinde belirtin.

## Katkıların lisansı

Katkıda bulunarak, katkınızın projenin lisansları altında yayımlanmasını kabul etmiş olursunuz: veri ve metinler (`data/`, `vault/`, `research/`, çeviriler) için [CC BY 4.0](LICENSE-DATA.md), kodlar (`tools/`, `viz/`) için [MIT](LICENSE). Alıntılar kendi konuşmacılarının sözleri olarak kalır. Adınız, değiştirdiğiniz dosyaların Git geçmişinde yer alır.
