// OCR a scanned PDF with macOS Vision, page by page.
// usage: swift tools/ocr.swift in.pdf out.txt [langs=tr-TR,en-US,fr-FR,de-DE] [firstPage] [lastPage]
// Each page is written as "=== page N ===" followed by recognised lines.
import Foundation
import PDFKit
import Vision
import AppKit

let a = CommandLine.arguments
guard a.count >= 3, let doc = PDFDocument(url: URL(fileURLWithPath: a[1])) else {
    print("usage: swift ocr.swift in.pdf out.txt [langs] [first] [last]"); exit(2)
}
let langs = a.count > 3 ? a[3].split(separator: ",").map(String.init) : ["tr-TR", "en-US", "fr-FR", "de-DE"]
let first = a.count > 4 ? Int(a[4])! : 1
let last = a.count > 5 ? min(Int(a[5])!, doc.pageCount) : doc.pageCount
var out = ""
for n in first...last {
    guard let page = doc.page(at: n - 1) else { continue }
    let box = page.bounds(for: .mediaBox)
    let scale: CGFloat = 2200 / max(box.width, box.height)
    let img = page.thumbnail(of: CGSize(width: box.width * scale, height: box.height * scale), for: .mediaBox)
    guard let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { continue }
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.recognitionLanguages = langs
    req.usesLanguageCorrection = true
    try? VNImageRequestHandler(cgImage: cg).perform([req])
    let lines = (req.results ?? []).compactMap { $0.topCandidates(1).first?.string }
    out += "=== page \(n) ===\n" + lines.joined(separator: "\n") + "\n"
    FileHandle.standardError.write("page \(n)/\(last)\n".data(using: .utf8)!)
}
try! out.write(toFile: a[2], atomically: true, encoding: .utf8)
