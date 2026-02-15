==========
Challenges
==========

Seasonal challenges and events.

Get Valentine 2026 Challenge Status
====================================

.. http:get:: /api/seasonal_challenges/valentine2026/status

   Get the status of the Valentine's Day 2026 challenge.

   **Query Parameters:**

   :is_in_japan: Boolean indicating if user is in Japan (required)

   **Example Request:**

   .. code-block:: http

      GET /api/seasonal_challenges/valentine2026/status?is_in_japan=true HTTP/1.1
      Host: www.wh00.ooo
      Authorization: Bearer <token>

   **Response:**

   :statuscode 200: Challenge status retrieved
   :statuscode 304: Not Modified (cached)

   .. code-block:: json

      {
        "challenge_id": "valentine2026",
        "is_active": true,
        "start_date": "2026-02-01T00:00:00+09:00",
        "end_date": "2026-02-14T23:59:59+09:00",
        "user_progress": {
          "completed": false,
          "current_step": 1,
          "total_steps": 5
        },
        "rewards": []
      }

Challenge Types
===============

Whoo features seasonal challenges including:

* **Valentine's Day**: Special location-based challenges
* **Holiday Events**: Seasonal activities and rewards
* **Location Challenges**: Visit specific places
* **Social Challenges**: Interact with friends

Challenge Structure
===================

Each challenge includes:

:challenge_id: Unique identifier
:is_active: Whether challenge is currently active
:start_date: Challenge start time
:end_date: Challenge end time
:user_progress: User's completion status
:rewards: Available rewards

Progress Tracking
=================

User progress includes:

.. code-block:: json

   {
     "completed": false,
     "current_step": 3,
     "total_steps": 5,
     "checkpoints": [
       {
         "id": 1,
         "name": "Visit a cafe",
         "completed": true
       },
       {
         "id": 2,
         "name": "Share location with friend",
         "completed": true
       }
     ]
   }

Rewards System
==============

Completing challenges unlocks:

* Custom app icons
* Special badges
* Premium features (temporary)
* In-app currency

**Reward Types:**

.. code-block:: json

   {
     "rewards": [
       {
         "type": "app_icon",
         "icon_id": 34,
         "icon_type": "sky_sweets_icon"
       },
       {
         "type": "badge",
         "badge_id": 100,
         "name": "Valentine's 2026"
       }
     ]
   }

Regional Challenges
===================

Some challenges are region-specific:

* ``is_in_japan`` parameter determines available challenges
* Different regions may have unique events
* Localized content and rewards

Best Practices
==============

.. tip::
   Check challenge status daily for new events.

.. tip::
   Cache challenge data to avoid repeated API calls.

.. note::
   Challenge availability may change based on user location.
