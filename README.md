# diqu-email

Alert module using Email method (Sendgrid)

## How to use

### Installation

```bash
pip install diqu diqu-email
```

### Send email

Before you can send email with Sendgrid, go create your template first:

- Go to Email API / Dynamic Templates: Create a Dyanmic Template
- Design your template e.g.

    ![sample template](/example/image.png)
- Save it and get the Template ID e.g. `d-c70732f1cb304d39823d52cd5cee8312`
- Go to Settings / API Keys: Get an API key e.g. SG.xxx.xxx

Now, you're ready to send alert:

```bash
export SENDGRID_API_KEY=YOURVALUE e.g. SG.xxx.xxx
export SENDGRID_MAILING_LIST=YOURVALUE e.g. dat@domain.com,dat2@domain.com
export SENDGRID_TEMPLATE_ID=YOURVALUE e.g. d-c70732f1cb304d39823d52cd5cee8312

# powershell
$env:SENDGRID_API_KEY="YOURVALUE"
$env:SENDGRID_MAILING_LIST="dat@domain.com,dat2@domain.com"
$env:SENDGRID_TEMPLATE_ID="d-c70732f1cb304d39823d52cd5cee8312"

diqu alert --to sendgrid
```

For a quick testing purpose, we can use the CSV package to run the [example](./example/) as following command:

```bash
diqu alert --to sendgrid --package csv --profile-name example --profiles-dir ./example
```

Here is the sample result:

![Alt text](/example/email.png)
