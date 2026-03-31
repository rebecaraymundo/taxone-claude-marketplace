"""
text_utils — Funcoes utilitarias de texto compartilhadas entre scripts.

Consolida: html_escape, normalize_key, normalize_for_match, strip_html.

Uso:
    from text_utils import html_escape, normalize_key, normalize_for_match, strip_html
"""

import re
import unicodedata
from html.parser import HTMLParser


# ── HTML escape/unescape ───────────────────────────────────────────────────

def html_escape(text) -> str:
    """Escapa caracteres especiais para HTML."""
    if not text:
        return ""
    return (str(text)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))


# ── Strip HTML ─────────────────────────────────────────────────────────────

class _HTMLStripper(HTMLParser):
    """Strip HTML tags and convert basic elements to plain text."""

    def __init__(self):
        super().__init__()
        self._parts = []
        self._in_li = False

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag == "br":
            self._parts.append("\n")
        elif tag == "p":
            self._parts.append("\n")
        elif tag == "li":
            self._parts.append("\n- ")
            self._in_li = True
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._parts.append("\n\n")
        elif tag in ("div", "tr"):
            self._parts.append("\n")

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "li":
            self._in_li = False
        elif tag in ("p", "div", "tr"):
            self._parts.append("\n")

    def handle_data(self, data):
        self._parts.append(data)

    def get_text(self):
        text = "".join(self._parts)
        # Normalizar multiplas linhas em branco
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def strip_html(html_text: str) -> str:
    """Converte HTML para texto simples.

    Usa HTMLParser para preservar quebras de linha e listas.
    Fallback com regex se o parser falhar.
    """
    if not html_text:
        return ""
    try:
        import html as html_mod
        html_text = html_mod.unescape(html_text)
    except Exception:
        pass
    try:
        stripper = _HTMLStripper()
        stripper.feed(html_text)
        return stripper.get_text()
    except Exception:
        # Fallback: regex strip
        text = re.sub(r"<br\s*/?>", "\n", html_text, flags=re.IGNORECASE)
        text = re.sub(r"<[^>]+>", "", text)
        return text.strip()


# ── Text normalization ─────────────────────────────────────────────────────

def remove_accents(text: str) -> str:
    """Remove acentos/diacriticos de um texto."""
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def normalize_key(text: str, upper: bool = False) -> str:
    """Normaliza texto para usar como chave de lookup.

    Remove acentos, pontuacao, normaliza espacos para underscore.

    Args:
        text: texto a normalizar
        upper: se True retorna UPPERCASE, senao lowercase (default)

    Returns:
        chave normalizada (ex: "Relatório Fiscal" -> "relatorio_fiscal")
    """
    text = remove_accents(text)
    text = text.upper().strip() if upper else text.lower().strip()
    text = re.sub(r"[\s-]+", "_", text)
    text = re.sub(r"[^\w]", "", text)
    return text


def normalize_for_match(text: str) -> str:
    """Normaliza texto para matching de caminhos funcionais.

    Uppercase, sem acentos, sem pontuacao (exceto >), espacos normalizados.

    Args:
        text: texto a normalizar (ex: "Básicos > Ferramentas")

    Returns:
        texto normalizado (ex: "BASICOS > FERRAMENTAS")
    """
    text = remove_accents(text)
    text = text.upper().strip()
    text = re.sub(r"[^A-Z0-9\s>]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
