import enum

STATUS = enum.Enum(
    'UNKNOWN',
    'SUCCESS',
    'FAILURE',
    'ABORTED',
    'DISABLED',
    'UNSTABLE',
    'NOT_BUILT',
    'BUILDING_FROM_UNKNOWN',
    'BUILDING_FROM_SUCCESS',
    'BUILDING_FROM_FAILURE',
    'BUILDING_FROM_ABORTED',
    'BUILDING_FROM_DISABLED',
    'BUILDING_FROM_UNSTABLE',
    'BUILDING_FROM_NOT_BUILT',
    'BUILDING_FROM_PREVIOUS_STATE',
    'POLL_ERROR',
    'INVALID_STATUS'
)
