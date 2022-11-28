import Editor from 'react-simple-code-editor'
import { highlight, languages } from 'prismjs/components/prism-core'
import 'prismjs/components/prism-lolcode'
import 'prismjs/themes/prism.css'
import language from 'react-syntax-highlighter/dist/esm/languages/hljs/1c'

export default function CodeEditor({
  code,
  handleValueChange,
  id,
  isTerminal,
  readOnly = false,
}) {
  // Apply syntax highlighting.
  const hightlightWithLineNumbers = (input, language) =>
    highlight(input, language)
      .split('\n')
      .map(
        (line, i) =>
          `${
            isTerminal ? '' : `<span class='editorLineNumber'>${i + 1}</span>`
          }${line}`
      )
      .join('\n')

  return (
    <div
      style={{
        minHeight: '60vh',
        height: '60vh',
        overflow: 'auto',
        backgroundColor: 'var(--black)',
        padding: '1rem',
        borderRadius: '0.4rem'
      }}
    >
      <Editor
        value={code}
        onValueChange={handleValueChange}
        highlight={(code) => hightlightWithLineNumbers(code, isTerminal? languages.text : languages.lolcode)}
        padding={10}
        textareaId={id}
        className="editor"
        readOnly={readOnly}
        placeholder={isTerminal? "" : "BTW enter your LOLCODE or upload a file..."}
        style={{
          fontFamily: '"Fira code", "Fira Mono", monospace',
          fontSize: 18,
          outline: 0,
          color: 'var(--light-grey)',
        }}
      />
    </div>
  )
}
