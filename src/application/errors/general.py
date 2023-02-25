from fastapi import Response, status, HTTPException


class GeneralError:
    def check_client_request(self, process: str, response: Response):
        if response.status_code not in [status.HTTP_200_OK, status.HTTP_201_CREATED]:
            raise HTTPException(
                status_code=response.status_code,
                detail={
                    'process': process,
                    'error': response.json()
                }
            )
