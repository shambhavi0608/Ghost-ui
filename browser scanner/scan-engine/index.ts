// src/scan-engine/index.ts

// Main Scan Engine Entry Point

export { runFullScan } from "./runScan";

// Main Result Type
export type {
  GhostScanResult,
  FingerprintResult,
  EntropyResult,
  StorageAuditResult,
  SystemSignals,
  CanvasFingerprintResult,
  WebGLFingerprintResult,
  FontDetectionResult,
} from "./types/scanResult.ts";

// Permission Types
export type {
  PermissionStateType,
  PermissionStatusMap,
  PermissionScanResult,
  SupportedPermission,
} from "./types/permission.ts";

// Tracker Types
export type {
  TrackerDefinition,
  TrackerInfo,
  TrackerDetectionResult,
  TrackerCategory,
  TrackerSummary,
  CategorizedTrackers,
} from "./types/tracker.ts";