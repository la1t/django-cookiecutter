{% raw -%}
{{/*
Create secret to access docker registry
*/}}
{{- define "app.pullSecret" }}
{{- printf "{\"auths\": {\"%s\": {\"auth\": \"%s\"}}}" .Values.pullSecret.registry (printf "%s:%s" .Values.pullSecret.username .Values.pullSecret.password | b64enc) | b64enc }}
{{- end }}

{{/*
Return the proper backend image name
*/}}
{{- define "backend.image" -}}
{{ include "common.images.image" ( dict "imageRoot" .Values.backend.image ) }}
{{- end -}}

{{/*
Render backend pullSecrets
*/}}
{{- define "backend.renderPullSecrets" -}}
imagePullSecrets:
- name: {{ include "common.names.fullname" . }}-pullsecret
{{- end -}}

{{/*
Return backend imagePullPolicy
*/}}
{{- define "backend.imagePullPolicy" -}}
{{ .Values.backend.image.pullPolicy }}
{{- end -}}

{{/*
Render full env for backend
*/}}
{{- define "backend.renderEnv" -}}
- name: DJANGO_DEBUG
  value: {{ .Values.backend.debug|quote }}

- name: DJANGO_ALLOWED_HOSTS
  value: {{ .Values.domain|quote }}

- name: DJANGO_DEFAULT_FROM_EMAIL
  value: {{ .Values.backend.defaultFromEmail|quote }}

- name: AWS_S3_ENDPOINT_URL
  value: {{ .Values.backend.s3.endpointUrl|quote }}

- name: AWS_ACCESS_KEY_ID
  value: {{ .Values.backend.s3.accessKey|quote }}

- name: AWS_SECRET_ACCESS_KEY
  value: {{ .Values.backend.s3.secretKey|quote }}

- name: AWS_S3_BUCKET_NAME
  value: {{ .Values.backend.s3.bucketName|quote }}

- name: AWS_S3_PUBLIC_URL
  value: {{ .Values.backend.s3.publicUrl|quote }}

- name: MAILGUN_SENDER_DOMAIN
  value: {{ .Values.backend.mailgun.senderDomain|quote }}

- name: MAILGUN_API_KEY
  value: {{ .Values.backend.mailgun.apiKey|quote }}

- name: SENTRY_DSN
  value: {{ .Values.backend.sentryDsn|quote }}

- name: SENTRY_ENVIRONMENT
  value: {{ .Values.backend.sentryEnvironment|quote }}

- name: DATABASE_URL
  value: {{ .Values.backend.postgresUrl|quote }}

{{- end -}}

{{/*
Render init container for migrations waiting
*/}}
{{- define "backend.waitMigrationsInitContainer" -}}
- name: {{ include "common.names.fullname" . }}-wait-migrations
  image: {{ include "backend.image" . }}
  imagePullPolicy: {{ include "backend.imagePullPolicy" . }}
  command:
  - python
  - manage.py
  - migrate
  - --check
  env: {{- include "backend.renderEnv" . | nindent 4 }}
  {{- if .Values.backend.waitMigrations.resources }}
  resources: {{- toYaml .Values.backend.waitMigrations.resources | nindent 4 }}
  {{- end }}
{{- end -}}
{%- endraw %}
