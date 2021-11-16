FROM python:3.8-slim

ARG USER_ID=1000
ARG DEV_MODE=0
ARG USER_NAME=emkademy
ARG ARTIFACT_STORE=/artifact-store

ENV HOME="/home/${USER_NAME}"
ENV \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV="${HOME}/venv" \
    PYTHONPATH="/app:${PYTHONPATH}" \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    BUILD_POETRY_LOCK="${HOME}/poetry.lock.build"

RUN apt-get -qq update \
    && DEBIAN_FRONTEND="noninteractive" apt-get -qq -y install git \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -qq -y clean

RUN addgroup --system --gid "${USER_ID}" "${USER_NAME}" \
    && adduser --system --home "${HOME}" --uid "${USER_ID}" --ingroup "${USER_NAME}" "${USER_NAME}"

RUN chown -R "${USER_NAME}" "${HOME}"
RUN mkdir /app && chown "${USER_NAME}" /app

RUN if [ $DEV_MODE -eq 1 ]; then \
        mkdir -p "${ARTIFACT_STORE}" && chown "${USER_NAME}" "${ARTIFACT_STORE}"; \
    fi

COPY ./docker/run-server.sh /
RUN chown -R ${USER_NAME} /run-server.sh && chmod +x /run-server.sh

RUN HOME=/tmp pip install --no-cache-dir poetry==1.1.11

USER "${USER_NAME}"
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

COPY ./pyproject.toml ./*.lock /app/
WORKDIR /app

RUN python3.8 -m venv $VIRTUAL_ENV \
    && if [ $DEV_MODE -eq 1 ]; then \
        pip install --upgrade pip \
        && poetry install \
        && cp poetry.lock "${BUILD_POETRY_LOCK}"; \
    else \
        [ -f poetry.lock ] || { echo 'No poetry.lock found' ; exit 1; }; \
        poetry install --no-dev; \
    fi \
    && rm -rf $HOME/.cache/*

CMD ["/run-server.sh"]
