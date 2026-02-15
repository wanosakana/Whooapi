=======
Premium
=======

Whoo Premium subscription features.

Get Premium User Status
=======================

.. http:get:: /api/whoo_premium/v2/premium_user

   Check if the user has an active premium subscription.

   **Request Headers:**

   .. code-block:: http

      Content-Type: application/json
      Authorization: Bearer <token>
      If-None-Match: W/"714e3f70a3eaa23b773825b0d176155d"

   **Response:**

   :statuscode 200: Premium status retrieved
   :statuscode 304: Not Modified (cached)

   .. code-block:: json

      {
        "is_premium": false,
        "premium_expires_at": null,
        "features": []
      }

Premium Features
================

Premium subscribers get access to:

* Advanced location tracking
* Unlimited spot history
* Custom app icons
* Ad-free experience
* Priority support

Subscription Status
===================

The premium status response includes:

:is_premium: Boolean indicating active subscription
:premium_expires_at: Expiration timestamp (ISO 8601)
:features: Array of enabled premium features

**Feature Types:**

* ``unlimited_spots``: No limit on saved spots
* ``custom_icons``: Access to premium app icons
* ``advanced_analytics``: Detailed location analytics
* ``ad_free``: No advertisements

Checking Premium Status
=======================

Check premium status on:

1. App launch
2. When accessing premium features
3. Periodically (e.g., daily)

**Example Check:**

.. code-block:: python

   import requests

   def check_premium_status(token):
       headers = {
           'Authorization': f'Bearer {token}',
           'Content-Type': 'application/json'
       }
       response = requests.get(
           'https://www.wh00.ooo/api/whoo_premium/v2/premium_user',
           headers=headers
       )
       if response.status_code == 200:
           data = response.json()
           return data.get('is_premium', False)
       return False

Subscription Management
=======================

.. note::
   Subscription purchases are handled through platform-specific stores (App Store, Google Play).

.. tip::
   Cache premium status but validate before accessing premium-only features.

.. warning::
   Always check premium status before enabling premium features client-side.
