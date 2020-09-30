# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple

from google.api_core import grpc_helpers  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google import auth  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.oslogin_v1 import common  # type: ignore
from google.cloud.oslogin_v1.types import oslogin
from google.protobuf import empty_pb2 as empty  # type: ignore

from .base import OsLoginServiceTransport, DEFAULT_CLIENT_INFO


class OsLoginServiceGrpcTransport(OsLoginServiceTransport):
    """gRPC backend transport for OsLoginService.

    Cloud OS Login API
    The Cloud OS Login API allows you to manage users and their
    associated SSH public keys for logging into virtual machines on
    Google Cloud Platform.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "oslogin.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        channel: grpc.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):	
                The client info used to send a user-agent string along with	
                API requests. If ``None``, then default info will be used.	
                Generally, you only need to set this if you're developing	
                your own client library.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        if channel:
            # Sanity check: Ensure that channel and credentials are not both
            # provided.
            credentials = False

            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
        elif api_mtls_endpoint:
            warnings.warn(
                "api_mtls_endpoint and client_cert_source are deprecated",
                DeprecationWarning,
            )

            host = (
                api_mtls_endpoint
                if ":" in api_mtls_endpoint
                else api_mtls_endpoint + ":443"
            )

            if credentials is None:
                credentials, _ = auth.default(
                    scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id
                )

            # Create SSL credentials with client_cert_source or application
            # default SSL credentials.
            if client_cert_source:
                cert, key = client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
            else:
                ssl_credentials = SslCredentials().ssl_credentials

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
            )
        else:
            host = host if ":" in host else host + ":443"

            if credentials is None:
                credentials, _ = auth.default(
                    scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id
                )

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_channel_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
            )

        self._stubs = {}  # type: Dict[str, Callable]

        # Run the base constructor.
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes or self.AUTH_SCOPES,
            quota_project_id=quota_project_id,
            client_info=client_info,
        )

    @classmethod
    def create_channel(
        cls,
        host: str = "oslogin.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            address (Optionsl[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        scopes = scopes or cls.AUTH_SCOPES
        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def delete_posix_account(
        self,
    ) -> Callable[[oslogin.DeletePosixAccountRequest], empty.Empty]:
        r"""Return a callable for the delete posix account method over gRPC.

        Deletes a POSIX account.

        Returns:
            Callable[[~.DeletePosixAccountRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_posix_account" not in self._stubs:
            self._stubs["delete_posix_account"] = self.grpc_channel.unary_unary(
                "/google.cloud.oslogin.v1.OsLoginService/DeletePosixAccount",
                request_serializer=oslogin.DeletePosixAccountRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_posix_account"]

    @property
    def delete_ssh_public_key(
        self,
    ) -> Callable[[oslogin.DeleteSshPublicKeyRequest], empty.Empty]:
        r"""Return a callable for the delete ssh public key method over gRPC.

        Deletes an SSH public key.

        Returns:
            Callable[[~.DeleteSshPublicKeyRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_ssh_public_key" not in self._stubs:
            self._stubs["delete_ssh_public_key"] = self.grpc_channel.unary_unary(
                "/google.cloud.oslogin.v1.OsLoginService/DeleteSshPublicKey",
                request_serializer=oslogin.DeleteSshPublicKeyRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_ssh_public_key"]

    @property
    def get_login_profile(
        self,
    ) -> Callable[[oslogin.GetLoginProfileRequest], oslogin.LoginProfile]:
        r"""Return a callable for the get login profile method over gRPC.

        Retrieves the profile information used for logging in
        to a virtual machine on Google Compute Engine.

        Returns:
            Callable[[~.GetLoginProfileRequest],
                    ~.LoginProfile]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_login_profile" not in self._stubs:
            self._stubs["get_login_profile"] = self.grpc_channel.unary_unary(
                "/google.cloud.oslogin.v1.OsLoginService/GetLoginProfile",
                request_serializer=oslogin.GetLoginProfileRequest.serialize,
                response_deserializer=oslogin.LoginProfile.deserialize,
            )
        return self._stubs["get_login_profile"]

    @property
    def get_ssh_public_key(
        self,
    ) -> Callable[[oslogin.GetSshPublicKeyRequest], common.SshPublicKey]:
        r"""Return a callable for the get ssh public key method over gRPC.

        Retrieves an SSH public key.

        Returns:
            Callable[[~.GetSshPublicKeyRequest],
                    ~.SshPublicKey]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_ssh_public_key" not in self._stubs:
            self._stubs["get_ssh_public_key"] = self.grpc_channel.unary_unary(
                "/google.cloud.oslogin.v1.OsLoginService/GetSshPublicKey",
                request_serializer=oslogin.GetSshPublicKeyRequest.serialize,
                response_deserializer=common.SshPublicKey.deserialize,
            )
        return self._stubs["get_ssh_public_key"]

    @property
    def import_ssh_public_key(
        self,
    ) -> Callable[
        [oslogin.ImportSshPublicKeyRequest], oslogin.ImportSshPublicKeyResponse
    ]:
        r"""Return a callable for the import ssh public key method over gRPC.

        Adds an SSH public key and returns the profile
        information. Default POSIX account information is set
        when no username and UID exist as part of the login
        profile.

        Returns:
            Callable[[~.ImportSshPublicKeyRequest],
                    ~.ImportSshPublicKeyResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_ssh_public_key" not in self._stubs:
            self._stubs["import_ssh_public_key"] = self.grpc_channel.unary_unary(
                "/google.cloud.oslogin.v1.OsLoginService/ImportSshPublicKey",
                request_serializer=oslogin.ImportSshPublicKeyRequest.serialize,
                response_deserializer=oslogin.ImportSshPublicKeyResponse.deserialize,
            )
        return self._stubs["import_ssh_public_key"]

    @property
    def update_ssh_public_key(
        self,
    ) -> Callable[[oslogin.UpdateSshPublicKeyRequest], common.SshPublicKey]:
        r"""Return a callable for the update ssh public key method over gRPC.

        Updates an SSH public key and returns the profile
        information. This method supports patch semantics.

        Returns:
            Callable[[~.UpdateSshPublicKeyRequest],
                    ~.SshPublicKey]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_ssh_public_key" not in self._stubs:
            self._stubs["update_ssh_public_key"] = self.grpc_channel.unary_unary(
                "/google.cloud.oslogin.v1.OsLoginService/UpdateSshPublicKey",
                request_serializer=oslogin.UpdateSshPublicKeyRequest.serialize,
                response_deserializer=common.SshPublicKey.deserialize,
            )
        return self._stubs["update_ssh_public_key"]


__all__ = ("OsLoginServiceGrpcTransport",)
