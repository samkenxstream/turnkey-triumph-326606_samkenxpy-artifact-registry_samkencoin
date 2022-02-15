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
# Generated code. DO NOT EDIT!
#
# Snippet for UpdateRepository
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-artifact-registry


# [START artifactregistry_generated_artifactregistry_v1beta2_ArtifactRegistry_UpdateRepository_sync]
from google.cloud import artifactregistry_v1beta2


def sample_update_repository():
    # Create a client
    client = artifactregistry_v1beta2.ArtifactRegistryClient()

    # Initialize request argument(s)
    request = artifactregistry_v1beta2.UpdateRepositoryRequest(
    )

    # Make the request
    response = client.update_repository(request=request)

    # Handle the response
    print(response)

# [END artifactregistry_generated_artifactregistry_v1beta2_ArtifactRegistry_UpdateRepository_sync]