import React from 'react'
import {
  ThemeProvider,
  Grid,
  Typography,
  Box,
  Chip,
  Table,
  TableBody,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from '@mui/material'
import { appTheme, StyledTableCell } from '../styles/theme'
import { Container } from '@mui/system'
import FileUploadIcon from '@mui/icons-material/FileUpload'
import ClearIcon from '@mui/icons-material/Clear'
import CategoryIcon from '@mui/icons-material/Category'
import CssBaseline from '@mui/material/CssBaseline'
import CodeEditor from '../components/CodeEditor'
import IconButton from '../components/IconButton'
import TerminalIcon from '@mui/icons-material/Terminal'

export default function Home() {
  const [code, setCode] = React.useState({ program: '' })
  const [success, setSuccess] = React.useState(false)
  const [lexemes, setLexemes] = React.useState()
  const [error, setError] = React.useState('')

  const imgSize = '112rem'

  // Fetch the starter code from the server.
  React.useEffect(() => {
    fetch('/start').then((res) =>
      res.json().then((data) => {
        setCode({
          program: data.program,
        })
      })
    )
  }, [])

  // Handle the upload of program file.
  const handleUpload = async (e) => {
    // Prevent from refreshing.
    e.preventDefault()

    // Read the contents of the file.
    const reader = new FileReader()
    reader.onload = async (e) => {
      const text = e.target.result
      setCode({ program: text })
    }

    reader.readAsText(e.target.files[0])
  }

  // Handle the fetching of data (POST).
  const handleInterpret = () => {
    fetch('/interpret', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ program: code }),
    }).then((res) => {
      res.json().then((data) => {
        console.log(data)
        // Store if interpretation is successful.
        setSuccess(Boolean(data['success']))

        // Store the corresponding data.
        if (success) {
          setLexemes(data['payload'])
          setError('')
        } else {
          setError(data['payload'])
          setLexemes([])
        }
      })
    })
  }

  return (
    <ThemeProvider theme={appTheme}>
      <CssBaseline />
      <Grid container sx={{ marginTop: 6 }}>
        {/* Start of Header */}
        <Grid item xs={1}></Grid>
        <Grid item xs={10}>
          <Container
            sx={{
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'center',
              alignItems: 'center',
            }}
          >
            <Box
              sx={{
                display: 'flex',
                flexDirection: 'row',
                alignItems: 'center',
              }}
            >
              <img src="./logo.png" width={imgSize} height={imgSize} />
              <Typography
                variant="h3"
                sx={{ marginLeft: '1rem', fontWeight: 700 }}
              >
                <span style={{ color: 'var(--orange-800)' }}>
                  &#60;lmao&#62;
                </span>
                code
              </Typography>
            </Box>
            <Chip
              sx={{ fontWeight: 600, marginTop: -1.2, marginBottom: '5rem' }}
              color="primary"
              variant="outlined"
              label="An esoteric programming interpreter"
            />
          </Container>
        </Grid>
        <Grid item xs={1}></Grid>
        {/* End of Header */}

        {/* Start of Body */}
        <Grid item xs={1}></Grid>
        <Grid item xs={5}>
          <Box sx={{ display: 'flex', flexDirection: 'column' }}>
            {/* Start of Editor */}
            <CodeEditor
              code={code.program}
              handleValueChange={(value) => setCode({ program: value })}
              id="codeArea"
            />
            {/* End of Editor */}

            {/* Start of Toolbar */}
            <Box
              sx={{
                display: 'flex',
                flexDirection: 'row',
                justifyContent: 'space-between',
                marginTop: '2rem',
              }}
            >
              <IconButton
                color="info"
                icon={<FileUploadIcon />}
                component="label"
                slot={
                  <div>
                    Upload File
                    <input
                      type="file"
                      hidden
                      onChange={(e) => handleUpload(e)}
                    />
                  </div>
                }
              />

              <IconButton
                color="error"
                icon={<ClearIcon />}
                handleClick={() => setCode({ program: '' })}
                slot="Clear"
              />

              <IconButton
                color="success"
                icon={<CategoryIcon />}
                handleClick={handleInterpret}
                slot="Execute"
              />
            </Box>
            {/* End of Toolbar */}

            {/* Start of Terminal */}
            <Typography
              variant="h5"
              sx={{
                marginTop: '4rem',
                marginBottom: '0.8rem',
                fontWeight: 700,
                letterSpacing: '0.04rem',
                color: 'var(--black)',
                display: 'flex',
                flexDirection: 'row',
                alignItems: 'center',
              }}
            >
              <TerminalIcon />
              <span
                style={{ marginLeft: '0.8rem', color: 'var(--orange-900)' }}
              >
                Terminal
              </span>
            </Typography>

            <CodeEditor
              code={!success && error ? error : ''}
              handleValueChange={() => {}}
              id="terminal"
              isTerminal
              readOnly
            />
            {/* End of Terminal */}
          </Box>
        </Grid>
        <Grid item xs={0.5}></Grid>

        <Grid item xs={4.5}>
          <Box sx={{ display: 'flex', flexDirection: 'column' }}>
            {/* Start of Lexer Table */}
            <TableContainer component={Paper} sx={{ height: '36rem' }}>
              <Table>
                {/* Start of Column Names */}
                <TableHead>
                  <TableRow>
                    <StyledTableCell>Lexeme</StyledTableCell>
                    <StyledTableCell>Type</StyledTableCell>
                    <StyledTableCell>Line</StyledTableCell>
                  </TableRow>
                </TableHead>
                {/* End of Column Names */}

                {/* Start of Table Body */}
                <TableBody>
                  {success && lexemes &&
                    Object.entries(lexemes).map((entry) => {
                      return entry[1].map((lex) => {
                        return (
                          <TableRow>
                            <StyledTableCell>{lex[0]}</StyledTableCell>
                            <StyledTableCell>{lex[1]}</StyledTableCell>
                            <StyledTableCell>{entry[0]}</StyledTableCell>
                          </TableRow>
                        )
                      })
                    })}
                </TableBody>
                {/* End of Table Body */}
              </Table>
            </TableContainer>
            {/* End of Lexer Table */}

            {/* Start of Semantics Table */}
            <TableContainer
              component={Paper}
              sx={{ marginTop: '4rem', height: '24rem' }}
            >
              <Table>
                {/* Start of Column Names */}
                <TableHead>
                  <TableRow>
                    <StyledTableCell>Name</StyledTableCell>
                    <StyledTableCell>Value</StyledTableCell>
                    <StyledTableCell>Type</StyledTableCell>
                  </TableRow>
                </TableHead>
                {/* End of Column Names */}

                {/* Start of Table Body */}
                <TableBody></TableBody>
                {/* End of Table Body */}
              </Table>
            </TableContainer>
            {/* End of Semantics Table */}
          </Box>
        </Grid>
        <Grid item xs={1}></Grid>
        {/* End of Body */}
      </Grid>

      {/* Margin */}
      <Box sx={{ marginBottom: '8rem' }}> </Box>
    </ThemeProvider>
  )
}
