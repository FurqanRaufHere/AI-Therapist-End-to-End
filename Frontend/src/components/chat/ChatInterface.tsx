// import React, { useState, useRef, useEffect } from 'react';
// import { Button } from '@/components/ui/button';
// import { Input } from '@/components/ui/input';
// import { Card } from '@/components/ui/card';
// import { Avatar, AvatarFallback } from '@/components/ui/avatar';
// import { ScrollArea } from '@/components/ui/scroll-area';
// import { Separator } from '@/components/ui/separator';
// import { Send, Brain, User, Loader2, RotateCcw } from 'lucide-react';
import React, { useState, useRef, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card } from '@/components/ui/card';
import { Avatar, AvatarFallback } from '@/components/ui/avatar';
import { ScrollArea } from '@/components/ui/scroll-area';
import { Separator } from '@/components/ui/separator';
import { Send, Brain, User, Loader2, RotateCcw } from 'lucide-react';
import { format } from 'date-fns';
import ReactMarkdown from 'react-markdown';

interface Message {
  id: string;
  content: string;
  isUser: boolean;
  timestamp: Date;
}

export function ChatInterface() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      content: "Hello! I'm your AI therapist. I'm here to provide you with mental health support and guidance. How are you feeling today?",
      isUser: false,
      timestamp: new Date(),
    },
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const scrollAreaRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLTextAreaElement>(null);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    if (scrollAreaRef.current) {
      const scrollContainer = scrollAreaRef.current.querySelector('[data-radix-scroll-area-viewport]');
      if (scrollContainer) {
        scrollContainer.scrollTop = scrollContainer.scrollHeight;
      }
    }
  }, [messages]);

  // Focus input on mount
  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  const handleSendMessage = async () => {
    if (!inputValue.trim() || isLoading) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      content: inputValue.trim(),
      isUser: true,
      timestamp: new Date(),
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      const response = await fetch('http://127.0.0.1:8000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userMessage.content }),
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.statusText}`);
      }

      const data = await response.json();

      const aiResponse: Message = {
        id: (Date.now() + 1).toString(),
        content: data.answer,
        isUser: false,
        timestamp: new Date(),
      };

      setMessages(prev => [...prev, aiResponse]);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: 'Sorry, there was an error processing your request. Please try again later.',
        isUser: false,
        timestamp: new Date(),
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleClearChat = () => {
    setMessages([
      {
        id: '1',
        content: "Hello! I'm your AI therapist. I'm here to provide you with mental health support and guidance. How are you feeling today?",
        isUser: false,
        timestamp: new Date(),
      },
    ]);
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <div className="h-screen flex flex-col bg-background">
      {/* Chat Header */}
      <div className="flex items-center justify-between p-4 border-b border-border bg-card">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 bg-gradient-therapeutic rounded-full flex items-center justify-center shadow-soft">
            <Brain className="w-6 h-6 text-white" />
          </div>
          <div>
            <h2 className="font-heading font-semibold text-lg text-foreground">
              AI Therapist
            </h2>
            <p className="text-sm text-muted-foreground">
              Always here to listen and support you
            </p>
          </div>
        </div>
        <Button
          variant="outline"
          size="sm"
          onClick={handleClearChat}
          className="text-muted-foreground hover:text-foreground"
        >
          <RotateCcw className="w-4 h-4 mr-2" />
          Clear Chat
        </Button>
      </div>

      {/* Messages Area */}
      <ScrollArea 
        ref={scrollAreaRef}
        className="flex-1 p-4"
      >
        <div className="space-y-6 max-w-4xl mx-auto">
          {messages.map((message) => (
            <div
              key={message.id}
              className={`flex items-start space-x-3 ${
                message.isUser ? 'flex-row-reverse space-x-reverse' : ''
              }`}
            >
              <Avatar className="w-8 h-8 flex-shrink-0">
                <AvatarFallback
                  className={`${
                    message.isUser
                      ? 'bg-primary text-primary-foreground'
                      : 'bg-gradient-therapeutic text-white'
                  } text-sm font-medium`}
                >
                  {message.isUser ? (
                    <User className="w-4 h-4" />
                  ) : (
                    <Brain className="w-4 h-4" />
                  )}
                </AvatarFallback>
              </Avatar>
              
              <div
                className={`flex-1 max-w-[70%] ${
                  message.isUser ? 'flex flex-col items-end' : ''
                }`}
              >
                <Card
                  className={`p-4 ${
                    message.isUser
                      ? 'bg-primary text-primary-foreground ml-8'
                      : 'bg-card border shadow-sm mr-8'
                  }`}
                >
                  <ReactMarkdown>
                    {message.content}
                  </ReactMarkdown>
                </Card>
                <p
                  className={`text-xs text-muted-foreground mt-2 ${
                    message.isUser ? 'text-right mr-8' : 'ml-0'
                  }`}
                >
                  {format(message.timestamp, 'h:mm a')}
                </p>
              </div>
            </div>
          ))}
          
          {/* Loading Indicator */}
          {isLoading && (
            <div className="flex items-start space-x-3">
              <Avatar className="w-8 h-8 flex-shrink-0">
                <AvatarFallback className="bg-gradient-therapeutic text-white text-sm font-medium">
                  <Brain className="w-4 h-4" />
                </AvatarFallback>
              </Avatar>
              <Card className="p-4 bg-card border shadow-sm mr-8">
                <div className="flex items-center space-x-2">
                  <Loader2 className="w-4 h-4 animate-spin text-primary" />
                  <p className="text-sm text-muted-foreground">
                    AI Therapist is typing...
                  </p>
                </div>
              </Card>
            </div>
          )}
        </div>
      </ScrollArea>

      <Separator />

      {/* Input Area */}
      <div className="p-4 bg-card">
        <div className="max-w-4xl mx-auto">
          <div className="flex space-x-3">
            <div className="flex-1">
              <textarea
                ref={inputRef}
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyDown={handleKeyPress}
                placeholder="Type your message here..."
                disabled={isLoading}
                aria-label="Chat input"
                autoComplete="off"
                spellCheck={false}
                rows={1}
                className="resize-none w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
              />
            </div>
            <Button
              onClick={handleSendMessage}
              disabled={isLoading || !inputValue.trim()}
              aria-label="Send message"
              className="flex items-center justify-center"
            >
              {isLoading ? <Loader2 className="w-5 h-5 animate-spin" /> : <Send className="w-5 h-5" />}
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}
