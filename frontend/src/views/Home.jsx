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
  Button,
  TextField,
} from '@mui/material'
import { appTheme, StyledTableCell } from '../styles/theme'
import { Container } from '@mui/system'
import FileUploadIcon from '@mui/icons-material/FileUpload'
import ClearIcon from '@mui/icons-material/Clear'
import CategoryIcon from '@mui/icons-material/Category'
import CssBaseline from '@mui/material/CssBaseline'
import CodeEditor from '../components/CodeEditor'

import Editor from 'react-simple-code-editor'
import { highlight, languages } from 'prismjs/components/prism-core'
import 'prismjs/themes/prism.css'

export default function Home() {
  const [code, setCode] = React.useState('')
  const imgSize = '112rem'

  // Handle the upload of program file.
  const handleUpload = async (e) => {
    // Prevent from refreshing.
    e.preventDefault()

    // Read the contents of the file.
    const reader = new FileReader()
    reader.onload = async (e) => {
      const text = e.target.result
      setCode(text)
      document.getElementById('code').value = text
    }

    reader.readAsText(e.target.files[0])
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
                sx={{ marginLeft: '0.8rem', fontWeight: 700 }}
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
              code={code}
              handleValueChange={(value) => setCode(value)}
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
              <Button
                variant="outlined"
                color="info"
                component="label"
                startIcon={<FileUploadIcon />}
                sx={{
                  marginRight: '1rem',
                  fontWeight: 700,
                }}
                disableElevation
                fullWidth
              >
                Upload Program
                {/* Input Field */}
                <input type="file" hidden onChange={(e) => handleUpload(e)} />
              </Button>

              <Button
                variant="outlined"
                color="error"
                startIcon={<ClearIcon />}
                onClick={() => setCode('')}
                sx={{
                  marginRight: '1rem',
                  fontWeight: 700,
                }}
                disableElevation
                fullWidth
              >
                Clear
              </Button>

              <Button
                variant="outlined"
                color="success"
                startIcon={<CategoryIcon />}
                sx={{ fontWeight: 700 }}
                disableElevation
                fullWidth
              >
                Execute
              </Button>
            </Box>
            {/* End of Toolbar */}

            {/* Start of Terminal */}
            <Typography
              variant="h5"
              sx={{
                marginTop: '4rem',
                marginBottom: '0.8rem',
                fontWeight: 700,
                textTransform: 'uppercase',
                letterSpacing: '0.04rem',
                color: 'var(--black)',
              }}
            >
              &#62;&#62;{' '}
              <span style={{ color: 'var(--orange-900)' }}>Terminal</span>
            </Typography>

            <CodeEditor
              code=''
              handleValueChange={() => {}}
              id='terminal'
              isTerminal
              readOnly
            />
            {/* End of Terminal */}
          </Box>
        </Grid>
        <Grid item xs={1}></Grid>

        <Grid item xs={4}>
          <Box sx={{ display: 'flex', flexDirection: 'column' }}>
            {/* Start of Lexer Table */}
            <TableContainer component={Paper} sx={{ height: '20rem' }}>
              <Table>
                {/* Start of Column Names */}
                <TableHead>
                  <TableRow>
                    <StyledTableCell>Lexeme</StyledTableCell>
                    <StyledTableCell>Type</StyledTableCell>
                    <StyledTableCell>Description</StyledTableCell>
                    <StyledTableCell>Line</StyledTableCell>
                  </TableRow>
                </TableHead>
                {/* End of Column Names */}

                {/* Start of Table Body */}
                <TableBody></TableBody>
                {/* End of Table Body */}
              </Table>
            </TableContainer>
            {/* End of Lexer Table */}

            {/* Start of Semantics Table */}
            <TableContainer
              component={Paper}
              sx={{ marginTop: '3rem', height: '20rem' }}
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
