/**
 * Transaction processors for the hardware-assets business network.
 * @param {org.sppu.hardware.AllocateHardware} tx
 * @transaction
 */
async function allocateHardware(tx) {
    const hardware = tx.hardware;
    if (hardware.status === 'ALLOCATED') {
        throw new Error('hardware is already allocated');
    }
    hardware.assignedTo = tx.employee;
    hardware.status = 'ALLOCATED';
    await getAssetRegistry('org.sppu.hardware.Hardware').then(registry => registry.update(hardware));
}

/**
 * @param {org.sppu.hardware.ReturnHardware} tx
 * @transaction
 */
async function returnHardware(tx) {
    const hardware = tx.hardware;
    hardware.assignedTo = null;
    hardware.status = 'AVAILABLE';
    await getAssetRegistry('org.sppu.hardware.Hardware').then(registry => registry.update(hardware));
}
