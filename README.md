# diqu-email

Alert module using Email method (Sendgrid)

## How to use

### Installation

```bash
pip install diqu diqu-email
```

### Send email

Before you can send email with Sendgrid, go create your template first:

TODO

Now, you're ready to send alert:

```bash
export SENDGRID_API_KEY=YOURVALUE e.g. sadghuwhjdshdakl
export SENDGRID_MAILING_LIST=YOURVALUE e.g. datnguyen.it09@gmail.com,datnguyen.it09+test@gmail.com
export SENDGRID_TEMPLATE_ID=YOURVALUE e.g. 12345

diqu alert --to sendgrid
```

For a quick testing purpose, we can use the CSV package to run the [example](./example/) as following command:

```bash
diqu alert --to sendgrid --package csv --profile-name example --profiles-dir ./example
```
