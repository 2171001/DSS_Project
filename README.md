<!-- What I Understood. -->
We're working on a project to develop a website that uses behavior and location analysis (BLA) to detect and prevent fraudulent transactions. The system will take information from the user during registration to identify unusual spending patterns or geographical areas, and will re-verify the identity if any surprising patterns are detected. After three invalid attempts, the system will block the user.

Designing a system to prevent fraudulent transactions and protect genuine user's credit card details can be a complex task. However, I can suggest some high-level steps to build such a system:
> User Registration
> Limit on Transaction Amount
> Behavioral and Location Analysis (BLA)
> Fraud Detection System (FDS)
> Transaction Monitoring
> Transaction Blocking
> User Verification
> Account Blocking
> User Notification

<!-- What Rahul requested. -->
During the transaction process of the user, his camera should capture his face and match it with the data we have in our database. If his face matches, he's a legitimate user. Or else we'll have to authenticate him.

<!-- Fraud Detecting Process. -->
But other than that, if any suspicious transaction patterns are found or if he is detected as a fraud, he'll be restricted from accessing the database (Website).

For accessing the website there are 3 attempts to authenticate. If all 3 attempts are failed, then the user account which is trying to access will be blocked.
