# 🔊 Sons do Quiz

## 📁 Estrutura de Arquivos

Coloque os arquivos de áudio nesta pasta:

```
static/sounds/
├── victory.mp3     # Som de vitória (quando ganha brinde)
├── defeat.mp3      # Som de derrota (quando não ganha brinde)
└── README.md       # Este arquivo
```

## 🎵 Formatos Suportados

- **MP3** (recomendado)
- **WAV**
- **OGG**

## 📏 Tamanho Recomendado

- **Máximo:** 2MB por arquivo
- **Duração:** 3-5 segundos
- **Qualidade:** 128kbps (MP3)

## 🎯 Como Usar

1. **Baixe os sons** que você quer usar
2. **Renomeie** para `victory.mp3` e `defeat.mp3`
3. **Cole** nesta pasta
4. **Os sons serão tocados automaticamente** na página de resultado

## 🔧 Configuração

Os sons são configurados automaticamente no arquivo `templates/resultado.html`
