# Docusign
it is the leading provider of electronic signature technology and contract lifecycle management solutions. 

## Credit Reward Redemption System 
### Functional Requirements
- users can view reward balances and redeem rewards
- rewards transactions are validated before processing
- aync processing for redemption that require additional checks (eg. fraud detections, etc.)
- notification of successful redemption
- support for high traffic spikes (eg. promotional campigns)

### Non Functional Requirements
- scalability: must handle 500K+ API requests per day
- low latency: API response times < 100ms
- security: supporting authentication, authorization and fraud checks
- cost-effective: optimize cloud storage for efficiency

### High level architecture
#### API INTERACTION 
- 1: API Layer (User Interaction) - Exposes REST/GraphQL apis to users
- 2: Authentication - uses OAuth2/JWT via AWS Cognito
- 3: Rate Limiting & Throttling - API gateway manages request limits per user
#### BACKEND MICROSERVICES

- 1: User Rewards Service
  - Fetches user Rewards Balances from DynamoDB or Redis cache
  
- 2: Redemption Service
  - Processes redemption requests
  - Sends transactions for validation via SQS for async processing
    
- 3: Fraud detection Services
  - Evaluates suspicious transactions using AI models and business rules
 
- 4: Notification Services
  - Sends email confirmations via SNS after successful redemption      


  
