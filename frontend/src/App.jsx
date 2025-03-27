import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [quote, setQuote] = useState({
    quote: 'Clique no botão para ver uma citação inspiradora...',
    author: '',
    category: ''
  })
  const [loading, setLoading] = useState(false)

  const fetchQuote = async () => {
    try {
      setLoading(true)
      const response = await fetch('http://127.0.0.1:8000/quote')
      if (!response.ok) {
        throw new Error('Erro ao buscar citação')
      }
      const data = await response.json()
      setQuote(data)
    } catch (error) {
      setQuote({
        quote: 'Erro ao carregar a citação. Tente novamente.',
        author: '',
        category: ''
      })
      console.error('Erro:', error)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchQuote()
  }, [])

  return (
    <div className="container">
      <h1>Citações Inspiradoras</h1>
      <div className="quote-card">
        <div className="quote-content">
          <p className="quote-text">{quote.quote}</p>
        </div>
        <div className="quote-info">
          <p className="quote-author">{quote.author && `- ${quote.author}`}</p>
          <p className="quote-category">{quote.category}</p>
        </div>
      </div>
      <button 
        className="new-quote-button"
        onClick={fetchQuote}
        disabled={loading}
      >
        {loading ? 'Carregando...' : 'Nova Citação'}
      </button>
    </div>
  )
}

export default App
